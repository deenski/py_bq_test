import argparse
from google.cloud import bigquery


def main(dataset):
    client = bigquery.Client()

    query = """
        SELECT first_name, last_name, country 
        FROM `""" + dataset + "`"

    query_job = client.query(query)  # Make an API request.

    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print(row[0] + " " + row.last_name + " " + row[2])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('dataset',
        help="project-id.dataset-name.table-name of your bigquery table")
    
    args = parser.parse_args()

    main(args.dataset)