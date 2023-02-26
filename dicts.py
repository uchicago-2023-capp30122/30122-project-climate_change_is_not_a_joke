
style_dict = {'display': 'inline-block',
              'text-align': 'center', 
              'font-family': 'Verdana',
              'color': '#4c9be8', 
              'width': '70%'}

# Commitment Amount Options

# max commitment
max_commitment_amount_tuples = [("$25k", "commitment_amount_sub25k"),
                     ("$50k", "commitment_amount_25_50k"),
                     ("$100k", "commitment_amount_100-500k"),
                     ("$500k", "commitment_amount_500k_1mil"),
                     ("$1mil", "commitment_amount_1_5mil"),
                     ("$5mil", "commitment_amount_5_25mil"),
                     ("$25mil", "commitment_amount_25_50mil"),
                     ("$50mil", "commitment_amount_50_100mil"),
                     ("No max", "commitment_amount_100mil")]

commitment_amount_columns = ["commitment_amount_sub25k", 
                             "commitment_amount_25_50k", 
                             "commitment_amount_100-500k", 
                             "commitment_amount_500k_1mil", 
                             "commitment_amount_1_5mil", 
                             "commitment_amount_5_25mil", 
                             "commitment_amount_25_50mil", 
                             "commitment_amount_50_100mil",
                             "commitment_amount_100mil"]

# min commitment
min_commitment_amount_tuples = {"$25k": "commitment_amount_sub25k", 
                                "$50k": "commitment_amount_25_50k",
                                "$100k": "commitment_amount_100-500k",
                                "$500k": "commitment_amount_500k_1mil",
                                "$1mil": "commitment_amount_1_5mil",
                                "$5mil": "commitment_amount_5_25mil",
                                "$25mil": "commitment_amount_25_50mil",
                                "$50mil": "commitment_amount_50_100mil"}             

# Dict: Country Name

# List: Climate Change Project Types
project_type = ["biodiversity",
                "adaptation and resilience", 
                "governance, legislation, and litigation",
                "climate, health, and environment",
                "environmental behaviour",
                "environmental economic theory",
                "environmental policy evaluation",
                "international climate politics",
                "science and impacts of climate change",
                "sustainable natural resources",
                "sustainable public and private finance",
                "transition to zero emissions growth"]
