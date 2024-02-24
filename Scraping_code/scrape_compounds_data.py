import requests
import json
import pandas as pd
import csv

df = pd.read_csv("/home/nady/Desktop/nawy_project/home_compound.csv")
compounds_id = df["id"].to_list()


csv_file_path = "detailed_compouned_data.csv"

columns = ["propertyID","propertyName", "propertyTypeID", "propertyTypeName",
          "compoundID", "areaID", "develperID", "finishing", "min_unit_area",
          "max_unit_area", "min_price", "max_price", "max_installment_years",
          "min_installments", "min_down_payment", "number_of_bathrooms", "number_of_bedrooms",
          "min_ready_by", "sponsored", "new_property", "company", "resale",
          "financing", "type", "has_offers", "offer_title", "limited_time_offer",
          "in_quick_search", "recommended", "manual_ranking", "completeness_score", 
          "ranking_type", "recommended_financing", "property_ranking", "compound_ranking",
          "tags"]

with open(csv_file_path, mode='a+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)


for compoundID in compounds_id:
  try:
    # start scraping code
    url = "https://webapi.cooingestate.com/api/properties/search?token=undefined&language=en&client_id=2094001443.1696698901"

    payload = json.dumps({
      "show": "property",
      "start": 1,
      "compounds_ids": [
        compoundID
      ]
    })
    headers = {
      'authority': 'webapi.cooingestate.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'origin': 'https://www.nawy.com',
      'referer': 'https://www.nawy.com/',
      'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Linux"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57',
      'X-API-Key': '{{token}}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_txt = response.text

    # Step 2: Parse the text into a Python dictionary using json.loads()
    parsed_data = json.loads(response_txt)
    
    for value in parsed_data["values"]:
      propertyID = value["id"]
      propertyName = value["name"]
      propertyTypeID = value["property_type"]["id"]
      propertyTypeName = value["property_type"]["name"]
      compoundID = value["compound"]["id"]
      areaID = value["area"]["id"]
      develperID = value["developer"]["id"]
      finishing = value["finishing"]
      min_unit_area = value ["min_unit_area"]
      max_unit_area = value ["max_unit_area"]
      min_price = value ["min_price"]
      max_price = value ["max_price"]
      max_installment_years = value ["max_installment_years"]
      min_installments = value ["min_installments"]
      min_down_payment = value ["min_down_payment"]
      number_of_bathrooms = value ["number_of_bathrooms"]
      number_of_bedrooms = value ["number_of_bedrooms"]
      min_ready_by = value ["min_ready_by"]
      sponsored = value ["sponsored"]
      new_property = value ["new_property"]
      company = value ["company"]
      resale = value ["resale"]
      financing = value ["financing"]
      type = value ["type"]
      has_offers = value ["has_offers"]
      offer_title = value ["offer_title"]
      limited_time_offer = value ["limited_time_offer"]
      in_quick_search = value ["in_quick_search"]
      recommended = value ["recommended"]
      manual_ranking = value ["manual_ranking"]
      completeness_score = value ["completeness_score"]
      ranking_type = value ["ranking_type"]
      recommended_financing = value ["recommended_financing"]
      property_ranking = value ["property_ranking"]
      compound_ranking = value ["compound_ranking"]
      tags = value ["tags"]

      # list of all extracted value
      values = [propertyID, propertyName, propertyTypeID, propertyTypeName, compoundID,
                areaID, develperID, finishing, min_unit_area, max_unit_area, min_price,
                max_price, max_installment_years, min_installments, min_down_payment,
                number_of_bathrooms, number_of_bedrooms, min_ready_by, sponsored, 
                new_property, company, resale, financing, type, has_offers, offer_title,
                limited_time_offer, in_quick_search, recommended, manual_ranking, 
                completeness_score, ranking_type, recommended_financing, property_ranking,
                compound_ranking, tags]
      with open(csv_file_path, mode='a+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(values)
  except Exception as e:
    print(e)
