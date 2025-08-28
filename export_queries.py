#!/usr/bin/env python3
import os, pandas as pd, psycopg2

DB = dict(host=os.getenv('PGHOST','localhost'),
          dbname=os.getenv('PGDATABASE','climate_monitoring'),
          user=os.getenv('PGUSER','postgres'),
          password=os.getenv('PGPASSWORD','postgres'),
          port=int(os.getenv('PGPORT',5432)))

QUERIES = {
    'kpi_monthly': 'SELECT * FROM kpi_monthly ORDER BY month;',
    'extreme_events_by_season': 'SELECT season, SUM(extreme_events) total_events FROM public.combined_data GROUP BY season ORDER BY total_events DESC;'
}

def run():
    conn = psycopg2.connect(**DB)
    out_dir = 'reports/sql_outputs'
    os.makedirs(out_dir, exist_ok=True)
    xlsx = os.path.join(out_dir, 'weekly_outputs.xlsx')
    with pd.ExcelWriter(xlsx) as writer:
        for name, q in QUERIES.items():
            df = pd.read_sql(q, conn)
            df.to_csv(os.path.join(out_dir, f'{name}.csv'), index=False)
            df.to_excel(writer, sheet_name=name, index=False)
    print(f"Exported {len(QUERIES)} datasets to {out_dir}")

if __name__ == '__main__':
    run()
