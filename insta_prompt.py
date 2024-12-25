

def create_caption_prompt(image_description, content_type, tone, additional_info=""):
    prompt = f"""
    Analyze the following image and generate an engaging Instagram caption and hashtags:

    Image Context: {image_description}
    Content Type: {content_type}
    Tone: {tone}
    Additional Information: {additional_info}

    Please create:

    1. A compelling Instagram caption that:
       - Starts with a hook or question to engage viewers
       - Includes 2-3 paragraphs of engaging content
       - Uses appropriate emojis strategically (2-3 per paragraph)
       - Matches the specified {tone} tone
       - Reflects the {content_type} content type
       - Incorporates any provided additional information
       - Ends with a clear call-to-action or engaging question

    2. A set of strategic hashtags that:
       - Includes 15-20 relevant hashtags
       - Mixes popular and niche hashtags
       - Groups hashtags by categories (e.g., industry, content type, brand-related)
       - Focuses on the {content_type} niche
       - Includes trending hashtags in the space
       - Maintains proper formatting with all hashtags in a block
       
    Format the output exactly like this in str format

    [ENGAGING OPENING HOOK/QUESTION]

    [MAIN CAPTION CONTENT WITH EMOJIS AND FORMATTING]

    [CALL TO ACTION OR QUESTION]

    [SPACE]

    [BLOCK OF HASHTAGS IN below FORMAT:] which is printed as by new line character
    #FirstHashtag #SecondHashtag #ThirdHashtag #NicheHashtag #ContentTypeHashtag #IndustryHashtag #TrendingHashtag #BrandHashtag #LocationHashtag #StyleHashtag #StrategyHashtag #CommunityHashtag #EngagementHashtag #NicheHashtag #CategoryHashtag

    Example desired output structure:

    Ever wondered why some Instagram posts go viral while others don't? 🤔

    Let me share a game-changing secret I discovered after analyzing 100+ viral posts! 🚀 The key isn't just in the quality of your content - it's in the timing and psychology of your audience. I've found that posts which combine authentic storytelling with strategic timing get 3x more engagement.

    #SocialMediaTips #InstagramStrategy #ContentCreator #SocialMediaMarketing #DigitalMarketing #InstagramGrowth #InstagramTips #MarketingStrategy #OnlineMarketing #BusinessGrowth #EntrepreneurMindset #PersonalBrand #InstagramExpert #CommunityGrowth #EngagementTips
    """
    return prompt

def generate_prompt(image_description, additional_description="", content_type="General", tone="Professional"):

    formatted_prompt = create_caption_prompt(
        image_description=image_description,
        content_type=content_type,
        tone=tone,
        additional_info=additional_description
    )
    
    return formatted_prompt