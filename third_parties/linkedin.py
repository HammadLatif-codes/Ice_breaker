import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profiles,
     Manually scrape information from linkedin profiles
    """
    api_key = "w_Qj55if9xLU_SRrUWgzcQ"
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {api_key}'}
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    # return response
    # gist_response = requests.get(
    #     "https://gist.githubusercontent.com/HammadLatif-codes/7599d01f3a8cd74d69ddd05512dd45de/raw/fe3e80bb1fc2b73b59864104df7b9d6c4d7e8f6d/bill-gates.json")
    #
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
