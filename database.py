from sqlalchemy import create_engine, text

# engine=create_engine("mysql+pymysql://root:Echakua189.@localhost/joviand_base")
# with engine.connect() as conn:
#     result=conn.execute(text('select * from jobs'))
#     print(result.all())
db_url="mysql+pymysql://root:Echakua189.@localhost/joviand_base"
engine = create_engine(
    db_url,
    connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result=conn.execute(text('select * from jobs'))
        jobs=[]
        for row in result.all():
            jobs.append(dict(row))
        return jobs
def load_job_from_db(id):
    with engine.connect() as conn:
        result=conn.execute(
            text("SELECT * FROM jobs WHERE id= :val"),
            val=id
        )
        rows=result.all()
        if len(rows)==0:
            return None
        else:
            return dict(rows[0])
