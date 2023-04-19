#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install facebook-sdk


# In[2]:


pip install facebook_business


# In[3]:


pip install gspread


# In[4]:


from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adaccountuser import AdAccountUser
app_id = '725277505999943'
app_secret = 'e5f048dab46f9ca31315c63cdb220833'
access_token = 'EAAKTotQb1EcBAGFmK9wssn46UApCGTxtjeaFBkZB8v5M0WlmquvWQmAeOUpNxOLIQdI0jHf7aI2eqbhKOG8ZBtKGAMVdJMcwlLG3J0TTGQKpBhrfgfQFyMCsEziFu1LS2BqIPTF2MJ7AHDidjgD64Je8AcuGiHKv3mcStqVc7ZBtzLVZAKQR4ZBklRNAA5bubkpfBOdprugZDZD'
FacebookAdsApi.init(app_id , app_secret , access_token)
me = AdAccountUser(fbid='me')
my_accounts = me.get_ad_accounts(fields=[AdAccountUser.Field.id])
account_ids = [account['id'] for account in my_accounts]
print(account_ids)


# In[5]:


import facebook
graph = facebook.GraphAPI(access_token)
for account_id in account_ids:
    account = AdAccount(account_id)
    campaigns = account.get_campaigns(fields=['name'], params={'status': ['ACTIVE', 'PAUSED']})
    campaign_ids = [campaign['id'] for campaign in campaigns]


# In[9]:


from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

FacebookAdsApi.init(access_token=access_token)

all_campaign_ids = []

for account_id in account_ids:
    account = AdAccount(account_id)
    campaigns = account.get_campaigns(fields=['name'])
    campaign_ids = [campaign['id'] for campaign in campaigns]
    all_campaign_ids.extend(campaign_ids)



# In[10]:


import datetime
from facebook_business.adobjects.campaign import Campaign
import pandas as pd
df_list = []

for campaign_id in all_campaign_ids:
    campaign = Campaign(campaign_id)
    
    end_time = datetime.datetime.now().strftime('2023-04-16')
    start_time = datetime.datetime.now().replace(month=1, day=1).strftime('2023-04-09')
    
    params = {
        'time_range': {'since': start_time, 'until': end_time},
        'time_increment': '1',
        'fields': [
            'account_name',
            'account_id',
            'campaign_name',
            'impressions',
            'clicks',
            'spend',
            'account_currency' ,
            'ctr',
            'cpc',
            'frequency',
            'reach',
            'inline_link_clicks',
            'full_view_impressions','optimization_goal']
    }
    
    insights = campaign.get_insights(params=params)
    df = pd.DataFrame(insights)
    df_list.append(df)


# In[11]:


import os
import pandas as pd
import datetime

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
file_name = "Report2_FB_" + date_string + ".csv"
folder_path = r"C:\Users\NHANDQ\Desktop\Report FB"
file_path = os.path.join(folder_path, file_name)
final_df = pd.concat(df_list)
final_df.to_csv(file_path, index=False)


# In[ ]:





# In[ ]:




