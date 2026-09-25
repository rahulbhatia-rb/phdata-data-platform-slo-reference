# phData Data Platform SLO Reference

Runnable publish gate for a data platform. It enforces freshness, task health, cost-anomaly review, and lineage evidence before downstream data is released.

```bash
python3 data_gate.py --self-test
python3 data_gate.py profile.json
```

Independent demonstration; not phData internal software.
