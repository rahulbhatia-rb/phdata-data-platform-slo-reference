# phData Data Platform SLO Reference

Runnable publish gate for a data platform. It enforces freshness, task health, cost-anomaly review, and lineage evidence before downstream data is released.

```bash
python3 data_gate.py --self-test
python3 data_gate.py profile.json
```

Independent demonstration; not phData internal software.

## Design review

The gate prevents a technically successful pipeline from publishing unreliable data. Freshness, task completion, cost variance, and lineage evidence are assessed together, with explicit reasons returned for any blocked publish. It can run after orchestration and before materializing a downstream dataset.
