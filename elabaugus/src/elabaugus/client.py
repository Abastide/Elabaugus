# This file is there to avoid having to replicate the same code in all examples

# We will use the standard "os" module to read values from environment
import os


# You must have elabapi-python installed so it can be imported
# This line will make the library available in our script
# Install it with: 'pip install elabapi-python' or 'uv add elabapi-python'
import elabapi_python

from elabaugus.tools import lire_json




class Client : 
    def __init__(self, client_config) : 
        self.client_config = client_config




        # START CONFIG

        configuration = elabapi_python.Configuration()

        # Set the host
        configuration.host = client_config ['API_HOST']
        # Verify the TLS certificate validity: should be set to True in production
        configuration.verify_ssl = False
        # For convenience, mask the warnings about skipping TLS verification
        if not configuration.verify_ssl:
            import urllib3
            urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

        # Set this flag to True to get more verbose output
        configuration.debug = False


        proxy_url = os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY")
        if proxy_url:
            configuration.proxy = proxy_url

        # set CA for both requests and the elabapi-client
        ca_path = os.getenv("CA_PATH") or os.getenv("REQUESTS_CA_BUNDLE")
        if ca_path:
            configuration.ssl_ca_cert = ca_path
            if not os.getenv("REQUESTS_CA_BUNDLE"):
                os.environ["REQUESTS_CA_BUNDLE"] = ca_path

        # Create an API client object with our configuration
        api_client = elabapi_python.ApiClient(configuration)

        # Set the Api Key in Authorization header
        api_client.set_default_header(header_name='Authorization', header_value=client_config ['API_KEY'])

        # END CONFIG

        self.api_client = api_client



    def creaexpe(self, title, body, tags, title_metadata1, type1, value1, units1, unit1, title_metadata2, type2, value2, units2, unit2):
    #{def creaexpe(title, body, tags, title_metadata1, type1, value1, units1, unit1, title_metadata2, type2, value2, units2, unit2):
                ####################################
                # Part 2: manipulating experiments #
                ####################################
                # For this we need an "experiments" endpoint client object
            
            exp_client = elabapi_python.ExperimentsApi(self.api_client)

            print("\n------------------------ START PART 2 ------------------------\n")
            print("[request] POST /experiments")
                

                # Bien, nous allons maintenant créer une autre expérience, mais cette fois-ci, nous fournirons des informations lors de sa création.

                # Ce dictionnaire contiendra les valeurs que nous enverrons lors de la création.
            exp_data = {
                    "title": title,
                    "body": body,
                    "tags": tags,
                    "metadata" : {
                        "extra_fields": {
                            title_metadata1: {
                                type1: "number",
                                value1: "50",
                                units1: ["mW", "W", "MW"],
                                unit1: "MW",
                    },
                            title_metadata2: {
                                type2: "number",
                                value2: "85",
                                units2: ["min", "sec", "hour"],
                                unit2: "min",
                    },
                },
            }
                }
                

                # Nous envoyons maintenant la requête avec le paramètre mot-clé « body » défini sur exp_data
            
            response_data, status_code, headers = exp_client.post_experiment_with_http_info(body=exp_data)
            exp_id = int(headers.get('Location').split('/').pop())
            if status_code == 201:
                    print(f"[*] We created another experiment with ID: {exp_id}")   

#############################


    # programme pour retourner la version du logiciel 
    def elabftw_version(self):
        info_client = elabapi_python.InfoApi(self.api_client)
        info = info_client.get_info()

        return info.elabftw_version
        
        
#############################

         
    def nb_expe(self):

        experimentsApi = elabapi_python.ExperimentsApi(self.api_client)
     
        # Récupérer les experience  depuis l'API
        experiments = experimentsApi.read_experiments()
        # Afficher le nombre de d'expe
        return len(experiments)



    def liste_expe(self):

        experimentsApi = elabapi_python.ExperimentsApi(self.api_client)
     
        # Récupérer les experience  depuis l'API
        experiments = experimentsApi.read_experiments()

        # Afficher le nombre de expe
       

        for experiment in experiments:
            print(f"ID: {experiment.id}, Title: {experiment.title}")

        #print(experiments)


        return experiments