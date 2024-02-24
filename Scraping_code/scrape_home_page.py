import requests
import json
import csv

page_no = 1
start = 1

# columns in csv {id, name_container, is_super, slug, properties_count, image_url, min_price,
# max_price, min_unit_area, max_unit_area, available_bathrooms, available_bedrooms, currency,
# sponsored, max_installment_years, min_down_payment, min_ready_by, sum_10_properties_min_price,
# lat, long, has_offer, offer_title, limited_time_offer}
## writting in csv file
columns  = ["id", "compound_name", "is_super", "slug", "properties_count", "image_url",
              "min_price", "max_price", "min_unit_area", "max_unit_area","available_bathrooms",
              "available_bedrooms", "developer_id", "developer_name", "developer_logo",
              "area_id", "area_name", "sponsored", "max_installment_years",
              "min_down_payment", "min_ready_by", "properties_ids",
              "sum_10_properties_min_price", "lat", "long", "has_offer", "has_launches",
              "is_launch", "offer_title", "limited_time_offer", 
              "property_types", "property_types_count"]

csv_file_path = "home_data.csv"

with open(csv_file_path, mode='a+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)

while True:
  web_page = "https://www.nawy.com/search?page_number=page_no"
  # send an http get request to url and retrieve the content
  response = requests.get(web_page)

  # Check if the requests was successful (status code 200)
  if response.status_code == 200:
    # parsing the json request of each pag 
    url = "https://webapi.cooingestate.com/api/properties/search?token=undefined&language=en&client_id=2094001443.1696698901"
    payload = json.dumps({
      "show": "compound",
      "start": start
      })
    headers = {
      'authority': 'webapi.cooingestate.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'origin': 'https://wwimagew.nawy.com',
      'referer': 'https://www.nawy.com/',
      'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Linux"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_txt = response.text
    # Step 2: Parse the text into a Python dictionary using json.loads()
    parsed_data = json.loads(response_txt)

    # Step 3: Encode the parsed data as JSON using json.dumps()
    #json_data = json.dumps(parsed_data, indent=4)  # Use indent for pretty formatting

    for value in parsed_data["values"]:
      id = value["id"]
      compound_name = value["name"]
      is_super = value["is_super"]
      slug = value["slug"]
      properties_count = value["properties_count"]
      image_url = value["image"]
      min_price = value["min_price"]
      max_price = value["max_price"]
      min_unit_area = value["min_unit_area"]
      max_unit_area = value["max_unit_area"]
      available_bathrooms = value["available_bathrooms"]
      available_bedrooms = value["available_bedrooms"]
      developer_id =  value["developer"]["id"]
      developer_name =  value["developer"]["name"]
      developer_logo = value["developer"]["logo_path"]
      area_id = value["area"]["id"]
      area_name = value["area"]["name"]
      sponsored = value["sponsored"]
      max_installment_years = value["max_installment_years"]
      min_down_payment = value["min_down_payment"]
      min_ready_by = value["min_ready_by"]
      properties_ids = value["properties_ids"]
      sum_10_properties_min_price = value["sum_10_properties_min_price"]
      lat = value["lat"]
      long = value["long"]
      has_offer = value["has_offer"]
      has_launches = value["has_launches"]
      is_launch = value["is_launch"]
      offer_title = value["offer_title"]
      limited_time_offer = value["limited_time_offer"]
      property_types = value["property_types"]
      property_types_count =value["property_types_count"]
      # generate a list of values
      values = [id, compound_name, is_super, slug, properties_count, image_url, min_price,
                max_price, min_unit_area, max_unit_area, available_bathrooms,
                available_bedrooms, developer_id, developer_name,  developer_logo, area_id,
                area_name, sponsored, max_installment_years,
                min_down_payment, min_ready_by, properties_ids,
                sum_10_properties_min_price, lat, long, has_offer, has_launches,
                is_launch,  offer_title, limited_time_offer,property_types, property_types_count]
      # writing values in csv
      with open(csv_file_path, mode='a+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(values)
    start += 12
    # increase the html_page
    page_no += 1
  else:
    break