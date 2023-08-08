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

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query=text("insert into applications (job_id, full_name, email, linkedin, work_experience, resume_url, education) values(:job_id, :full_name, :email, :linkedin, :work_experience, :resume_url, :education)")
        conn.execute(query,job_id=job_id, 
                     full_name=data['full_name'],
                     linkedin=data['linkedin'],
                     email=data['email'],
                     work_experience=data['work_experience'],
                     resume_url=data['resume_url'],
                     education=data['education']
                     )

