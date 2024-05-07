# Airflow-PostgresSQL-to-S3

# Airflow Project for Exporting Files to MinIO 🔗

This project utilizes Apache Airflow to export files from PostgreSQL to an Amazon S3 compatible storage, MinIO, which is hosted locally.

## Installation

Make sure you have Docker installed on your machine. Then, clone the repository and navigate to the project directory.

1. Clone the repository:
   ```bash
   git clone https://github.com/Daws23/Airflow-PostgresSQL-to-S3.git
   ```
2. Navigate to the project directory:
   ```bash
     cd Airflow-PostgresSQL-to-S3
Follow the usage steps for initial and development set ups in usage.
## Usage

### Initialize Airflow
Use the following command to initialize Airflow:

```bash
docker-compose -f docker-compose.yaml up -d airflow-init
```

### Run/Rerun Airflow
Use the following command to run the cnotainer services(Airflow/PostgresSQL/MinIO):

```bash
docker-compose -f docker-compose.yaml up -d
```

### Stop Airflow
Use the following command to stop Airflow container services:

```bash
docker-compose -f docker-compose.yaml down
```

Before you follow these steps make sure you have downloaded the [Orders.csv](https://drive.google.com/file/d/1YBSmSkniOblRrYy0sua2PHmkyXURvYv4/view?usp=sharing)

That's it navigate to the Airflow UI to run and check the DAG execution and navigate to the MinIO's UI to check for the saved data. Happy Learning 📄🖍️o(≧o≦)o🧸!
