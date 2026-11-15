# Hosted Cloud scaling: 500 users versus 500 simultaneous browsers

**Actual public beta capacity: two isolated Chromium workers across two Linux service slots, not 500.**

Browser Core's free Hosted Cloud beta uses one Linux identity and encrypted temporary
browser storage per active account, isolated by systemd cgroups. It is currently
hosted on a single VDSKA VPS with 8 vCPU, 16 GB RAM and 200 GB disk. Public limits:
one Cloud browser per account, a 30-minute lease, at most 120 Cloud minutes per
account per day, and **two simultaneous Cloud browser slots**.

## What happens with 500 registrations?

Registrations are not a Cloud concurrency limit. 500 accounts can exist
independently, but at most two can actively use hosted Chromium simultaneously.
When the pool is full today, profile_create in cloud mode responds with a
capacity error. There is **no durable waitlist, guaranteed start time or
automatic node provisioning today**. Local and bring-your-own-server workers
remain independent choices. Cloud profile storage is ephemeral, not persistent.

## Proposed scale-out design

1. Separate the OAuth/MCP control plane from the browser worker fleet. It must
   never host untrusted client Chrome inside the same shared process.
2. Add a durable, **bounded, owner-scoped admission queue** with visible queue
   position, cancellation, lease expiry and fair per-account allocation.
   Do not hold long HTTP/MCP tool calls open while waiting for minutes.
3. Use a cluster scheduler on multiple dedicated worker nodes. Each run
   allocates a dedicated OS identity, storage, CPU/memory/pid quota and
   verified egress rules. Never expose other tenants' profiles, Docker sockets,
   host services or internal metadata endpoints to an untrusted webpage.
4. On verified worker heartbeat, dispatch the next eligible account from the
   queue. Revoke worker identity and securely clean ephemeral storage after
   expiry, user release or crashed heartbeat.
5. Scale worker nodes only after load tests and cost/accounting thresholds.
   At no point should a registration automatically trigger paid infrastructure.
6. Add metered billing only after merchant approval, refunds, idempotent
   order settlement and legally reviewed seller documentation.

## Capacity estimation (not a promise)

Let **C** be measured concurrent Cloud browser sessions. Registration count
alone is not sufficient: 500 accounts with two active browsers need two slots,
while 500 simultaneous sessions require roughly 500 isolated browser slots.

Per-slot requirements vary with the websites and workloads. A first-pass node
quota might reserve up to approximately 0.85 vCPU and 1.25 GiB RAM per
Chromium worker, but this is a resource limit, not a guaranteed capacity
benchmark. Cluster size requires peak-concurrency, failure-domain and
headroom testing. A single 8-vCPU, 16-GB host cannot safely run 500
concurrent browsers.

## Production gates

- Successful two-tenant and third-tenant-rejected end-to-end MCP test
- Strict account-to-worker routing, auth expiration, revocation and teardown
- SSRF and blocked private-network tests, cross-tenant attack suite
- Queue fairness and load tests across multiple worker hosts
- 24/7 worker monitoring, failure recovery and storage lifecycle controls
- Actual resource-minute metering and enforcement of billing-free trial quotas
- Signed installers and independent security review as appropriate

**Beta status (15 Nov 2026):** two isolated slots and basic quota enforcement
are implemented and tested; multi-node autoscaling, durable queue,
commercial checkout and 500-way concurrency are **not implemented**.

Project: https://browser.m2g.pro/
