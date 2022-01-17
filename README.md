# Home Assistant eBay Seller Integration


### Adds the following sensors
* Current orders needing to be shipped out
* Current orders needing to be shipped out <strong>today</strong>
* Available Funds
* Total Funds
* Funds on Hold
* Funds Processing

### Setup

- #### Add this integration to to your config/custom_components folder and restart your Home Assistant

- #### Follow the steps below to setup an eBay developer account.
1. Sign up for eBay developer account at [https://developer.ebay.com/signin](https://developer.ebay.com/signin)
2. Create a keyset. [Application Access Keys](https://developer.ebay.com/my/keys)
3. Save the Production App ID (Client ID) for later.
4. Save the Production Cert ID (Client Secret) for later.
5. [Go to the Auth Tokens for eBay page (Under Hi Username). Make sure you have the production enironment selected, then alerts and Nofications](https://developer.ebay.com/my/push?env=production&index=0)
6. Select the "Marketplace Account Deletion", then toggle the "Exempted from Marketplace Account Deletion", and select the "I do not persist eBay Data" <strong>More on this later</strong>
7. Go to User Tokens (eBay Sign-in)
8. Select the "Get Token from eBay Via Your Application"
9. Click on Add eBay Redirect URL
10. Add whatever display Title you would like. Example: "Home Assistant"
11. Add whatever privacy policy url you would like. (Not sure if this is actually required, but you could put home assistant's privacy policy url if needed)
12. In the "Your auth accepted URL" box you'll need to put the callback url for your home assistan in this format "https://{home assistant url}/auth/external/callback". (Example: https://blahblahblahblah.duckdns.org/auth/external/callback)
13. You can leave the "Your auth declined" blank.
14. Select OAuth instead of Auth'n'Auth
15. After saving make sure the OAuth Enabled has a checkmark next the display title you just created.
16. Save the "RuName (eBay Redirect URL name)" for later.

- #### Add the following entry within configuration.yaml using the things you saved from the previous section and then restart your home assistant.

```yaml
ebay:
  client_id: blahblahblah-PRD-sdlfkjsdf-2lkjsdfl #Saved from step 3
  client_secret: PRD-sdflkjsdf-sdfk-2345-al34-sd12 #Saved from step 4
  redirect_uri: blahblahblah-blahbla-blahbla-sdkljsd #Saved from step 16
```

- #### Add the integration within the Home Assistant integration page.
1. Go to Configuration
2. Devices & Services
3. Add the ebay integration.
4. It should redirect you to log into your eBay account.
5. Select I Agree

- #### You should now see the sensors within Home Assistant.


##### Marketplace Account Deletion Warning
I don't actually know whether or not you should be marking the exempted from marketplace account deletion (Mentioned in step 6). The only data we are saving is your own auth token the numbers saved within the sensors. We aren't saving any buyer data and if you delete your own ebay account you should understand that you would also need to then delete the integration. 


I believe it is possible to set up home assistant to deal with the marketplace account deletion notifications. However eBay sends the notification for every single account that is deleted, which would lead to unnecessary calls to your HA server. I haven't counted but it most likely wouldn't be an obsurd number that would bug down the server too much. But it is something to think about. I actually run another website that uses the integration and handles the marketplace account deletion so I have never marked the being exempt from marketplace account deletion. If you get any notices from eBay saying you are non-compliant because you incorrectly stated you didn't save user data please put in an issue and I'll see if this is worth putting in the integration. Alternatively if anyone wants to add this and create a pull request for it that would be apprecated as well.
