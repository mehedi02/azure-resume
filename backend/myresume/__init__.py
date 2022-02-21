import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, counter: func.DocumentList, updatedcounter: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # logging.info(counter[0]["count"])
    
    count = counter[0]["count"]
    count_dict = {"count": count}
    count_json = json.dumps(count_dict)

    updated_count = count + 1
    out_dict = {"id": "1","count": updated_count}
    out_json = json.dumps(out_dict)


    updatedcounter.set(func.Document.from_json(out_json))

    return func.HttpResponse("{}".format(count_json))

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
