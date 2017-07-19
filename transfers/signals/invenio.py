#!/usr/bin/env python

# Send the status to Invenio. You can setup the IP in the config variable
# at the top of this file.

import requests
import sys

INVENIO_URL = "http://web:5000"
INVENIO_ACCESS_TOKEN = "change me"
"""IP addresse of the Invenio server."""

def main(path, unit_type, status, uuid, accession_id):
    if unit_type == "ingest" and status == "PROCESSING":
        status = "AIP_PROCESSING"
    params = {
        "accession_id": accession_id,
        "status": status
    }
    if uuid and uuid != "None":
        params["archivematica_id"] = uuid
    url = "{base}/api/oais/archive/{accession_id}/".format(
        base=INVENIO_URL,
        accession_id=accession_id)
    response = requests.patch(
        url,
        json=params,
        headers={"Authorization": "Bearer " + INVENIO_ACCESS_TOKEN})
    if not response.ok:
        print("{code}: {reason}:\n{message}".format(
              code=response.status_code,
              reason=response.reason,
              message=response.text))
        return 1


if __name__ == "__main__":
    path = sys.argv[1]
    unit_type = sys.argv[2]  # String
    status = sys.argv[3]
    uuid = sys.argv[4]
    accession_id = sys.argv[5]
    sys.exit(main(path, unit_type, status, uuid, accession_id))
