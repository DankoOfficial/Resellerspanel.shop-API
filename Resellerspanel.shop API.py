# Made by DankoOfficial on Github
# Discord: $ky#3788
# Dont skid, I'll catch you I swear. Give credits
# .order | Create an order to a service
# .status | Check your order's status
# .services | Check the available services

import discord
from requests import post
from discord.ext import commands
ApiKey = "" # This is where you put your API key
client = commands.Bot(command_prefix=".") # You can change the dot as prefix to anything you want
discordBot = 'Discord Bot Token' # Edit this to your Bot Token
def updateBalance(): # Update the balance
    try: # Try to update the balance
        balance = (post('https://resellerspanel.shop/api/v2',json={"key":ApiKey,"action":"balance"}).json()['balance']) # Get the balance
        return balance # Return the balance
    except: # If error, return 0
        balance = "Unknown" # Set the balance to unknown
        return balance # Return the balance
def translate(service): # Translate the text
    if service == "47": service = "Instagram Followers" # If the service is 47, set the service to Instagram Followers
    elif service == "48": service = "Instagram Likes" # If the service is 48, set the service to Instagram Likes
    elif service == "22": service = "Instagram Views" # If the service is 22, set the service to Instagram Views
    elif service == "848": service = "Instagram Comment Likes" # If the service is 848, set the service to Instagram Comment Likes
    elif service == "681": service = "Tiktok Followers" # If the service is 681, set the service to Tiktok Followers
    elif service == "15": service = "Tiktok Likes" # If the service is 15, set the service to Tiktok Likes
    elif service == "14": service = "Tiktok Views" # If the service is 14, set the service to Tiktok Views
    elif service == "646": service = "Telegram Group Members" # If the service is 646, set the service to Telegram Group Members
    elif service == "38": service = "Telegram Post Reaction" # If the service is 38, set the service to Telegram Post Reaction
    elif service == "842": service = "Twitter Followers" # If the service is 842, set the service to Twitter Followers
    elif service == "40": service = "Twitter Likes" # If the service is 40, set the service to Twitter Likes
    elif service == "41": service = "Twitter Views" # If the service is 41, set the service to Twitter Views
    elif service == "42":service = "YouTube Views" # If the service is 42, set the service to YouTube Views
    elif service == "657": service = "Spotify Plays" # If the service is 657, set the service to Spotify Plays
    else: service = "Unknown" # If the service is unknown, set the service to unknown
    return service # Return the service
@client.command() # This is the command
async def order(ctx, *, service): # This is the command
    try: # Try to order the service
        cleanedMessage = ctx.message.content.replace(".order ", "") # Remove the command from the message
        list = cleanedMessage.split(" ") # Split the message into a list
        service = list[0] # Get the service
        link = list[1] # Get the link
        amount = list[2] # Get the amount
        print('Ordering ' + amount + ' ' + translate(service) + ' from ' + link) # Print the order
        give = post('https://resellerspanel.shop/api/v2',json={"key": ApiKey, "action": "add", "service": service, "link": link, "quantity": amount}) # Order the service
        embedVar = discord.Embed(title="Order Placed", color=0x38d13b) # Create the embed
        embedVar.add_field(name="Service", value=translate(service), inline=True) # Add the service
        embedVar.add_field(name="Link", value=link, inline=True) # Add the link
        embedVar.add_field(name="Amount", value=amount, inline=True) # Add the amount
        embedVar.add_field(name=f"Order ID", value=give.json()['order'], inline=True) # Add the order ID
        embedVar.set_footer(text="Order Placed") # Set the footer
        await ctx.send(embed=embedVar) # Send the embed
        print(f" - New order | Service: {translate(service)} | Link: {link} | Amount: {amount} | Order ID: {give.json()['order']} | User: {ctx.author.name} | ${updateBalance()} Left in your account") # Print the order
    except: # If error, print the error
        await ctx.send(f"Error at ordering your service. Did you use the format: .order <service> <link> <amount>\n`{give.json()['error']}`") # Send the error
        print(" - Failed to order | User: " + ctx.author.name + " | " + give.json()['error']) # Print the error
@client.command() # This is the command
async def status(ctx, *, status): # This is the command
    try: # Try to check the status
        status = post('https://resellerspanel.shop/api/v2', json={"key": ApiKey,"action": "status", "order": status}).json() # Check the status
        embedVar = discord.Embed(title="Order Status", color=0x38d13b) # Create the embed
        embedVar.add_field(name="Order Status", value=status['status'], inline=True) # Add the status
        embedVar.add_field(name="Remaining", value=status['remains'], inline=True) # Add the remaining
        await ctx.send(embed=embedVar) # Send the embed
        print(f" - Order status | Status: {status['status']} | Remaining: {status['remains']} | User: {ctx.author.name}") # Print the status
    except: # If error, print the error
        await ctx.send('Order not found') # Send the error

@client.command() # This is the command
async def services(ctx): # This is the command
    embedVar = discord.Embed(title="Services", color=0xFF0000) # Create the embed
    embedVar.add_field(name="Instagram", value='—————————————————————', inline=False) # Add the breakline
    embedVar.add_field(name="47", value=':rocket: Instagram Followers', inline=True) # Add the service
    embedVar.add_field(name="48", value=':rocket: Instagram Likes', inline=True) # Add the service
    embedVar.add_field(name="22", value=':rocket: Instagram Views', inline=True)# Add the service
    embedVar.add_field(name="848", value=':rocket: Instagram Comment Likes', inline=True) # Add the service
    embedVar.add_field(name="Tiktok", value="—————————————————————", inline=False) # Add the breakline
    embedVar.add_field(name="681", value=':rocket: Tiktok Followers', inline=True) # Add the service
    embedVar.add_field(name="15", value=':rocket: Tiktok Likes', inline=True) # Add the service
    embedVar.add_field(name="14", value=':rocket: Tiktok Views', inline=True) # Add the service
    embedVar.add_field(name="Telegram", value="—————————————————————", inline=False) # Add the breakline
    embedVar.add_field(name="846", value=':rocket: Telegram Group Members', inline=True) # Add the service
    embedVar.add_field(name="38", value=':rocket: Telegram Post Reaction', inline=True) # Add the service
    embedVar.add_field(name="Twitter", value="—————————————————————", inline=False) # Add the breakline
    embedVar.add_field(name="842", value=':rocket: Twitter Followers', inline=True) # Add the service
    embedVar.add_field(name="40", value=':rocket: Twitter Likes', inline=True) # Add the service
    embedVar.add_field(name="41", value=':rocket: Twitter Views', inline=True) # Add the service
    embedVar.add_field(name="YouTube", value="—————————————————————", inline=False) # Add the breakline
    embedVar.add_field(name="42", value=':rocket: YouTube Views', inline=True) # Add the service
    embedVar.add_field(name="Spotify", value="—————————————————————", inline=False) # Add the breakline
    embedVar.add_field(name="657", value=':rocket: Spotify Plays', inline=True) # Add the service
    await ctx.send(embed=embedVar) # Send the embed
try: client.run(discordBot) # Try to run the bot
except: print("Are you sure you inputted the correct token?") # Print the error
