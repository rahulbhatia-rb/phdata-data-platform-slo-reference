import json,sys
from pathlib import Path
def check(x):
 r=[]
 if x['freshness_minutes']>x['max_freshness_minutes']: r.append('data freshness SLA breached')
 if x['failed_tasks']: r.append('pipeline tasks failing')
 if x['warehouse_cost_delta']>.15: r.append('cost anomaly requires review')
 if not x['lineage_verified']: r.append('lineage evidence missing')
 return {'publish_data':not r,'reasons':r}
if __name__=='__main__':
 if sys.argv[1:]==['--self-test']: assert check({'freshness_minutes':4,'max_freshness_minutes':15,'failed_tasks':0,'warehouse_cost_delta':.02,'lineage_verified':True})['publish_data'];print('data platform SLO: passed')
 else: print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())),indent=2))
