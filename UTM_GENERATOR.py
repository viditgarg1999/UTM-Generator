#!/usr/bin/env python
# coding: utf-8

# In[ ]:


url=input("Enter the website url: ")                  # The full website URL (e.g. https://www.example.com)
campaign_source=input("Enter the Campaign Source: ")  #The referrer: (e.g. google, newsletter,facebook,reddit)
campaign_medium=input("Enter the campaign medium: ")  #Marketing medium: (e.g. cpc, banner, email,dailypost)
campaign_name=input("Enter campaign name: ")          #Product, promo code, or slogan (e.g. spring_sale)
campaign_term=input("Enter campaign content: ")       #Identify the paid keywords
campaign_content=input("Enter campaign term: ")       #Use to differentiate ads

generated_url=url

"""
Instructions:
1. Campaign_source is mandatory field, it helps you to track the source from where you are getting traffic
2. Campaign_medium is not mandatory but it is highly recommended to not to left it empty as it helps to predict the medium from where you are getting the traffic eg. it can be posts, newsletters, emails e.t.c
3. Remaining three fields "name,term,content" are not much important but again it completly depends upon your requirement, like if you want to filter the traffic as per name, term or content then you can fill up the values here
"""

if campaign_source:
    generated_url=generated_url+'?utm_source='+campaign_source
    if campaign_medium:
        generated_url=generated_url+'&utm_medium='+campaign_medium
    if campaign_name:
        generated_url=generated_url+'&utm_campaign='+campaign_name
    if campaign_term:
        generated_url=generated_url+'&utm_term='+campaign_term
    if campaign_content:
        generated_url=generated_url+'&utm_content='+campaign_content
    print("\n")
    print("Generated url is:""\n"+ generated_url)
else:
    print("\n")
    print("Campaign Source cannot be empty!!")
          

"""
Information about parameters:
1. Use utm_source to identify a search engine, newsletter name, or other source.
Example: google

2. Use utm_medium to identify a medium such as email or cost-per- click.
Example: cpc

3. Used for keyword analysis. Use utm_campaign to identify a specific product promotion or strategic campaign.
Example: utm_campaign=spring_sale

4. Used for paid search. Use utm_term to note the keywords for this ad.
Example: running+shoes

5. Used for A/B testing and content-targeted ads. Use utm_content to differentiate ads or links that point to the same URL.
Examples: logolink or textlink

"""

#Just copy the generated url and enjoy tracking.


# In[ ]:





# In[ ]:




