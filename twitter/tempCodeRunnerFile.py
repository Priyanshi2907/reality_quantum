main_df = pd.DataFrame()

for related_keyword in related_keywords:

    print(related_keyword)

    df = twitter_search(related_keyword)
    influencers=real_estate_influencers()
    print (df)
    print("influencers : ",influencers)
    
    if not df.empty:
        
        main_df = pd.concat([main_df, df], axis=0)
        
main_df.reset_index(drop=True, inplace=True)      

main_df
