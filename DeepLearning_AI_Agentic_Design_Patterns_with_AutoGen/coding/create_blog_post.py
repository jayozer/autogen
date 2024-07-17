# filename: create_blog_post.py
blog_title = "The Impact of Fluoride on Infants: Benefits and Risks"
intro = ("Fluoride has often been a topic of discussion when it comes to dental care in infants. "
         "While fluoride is known for its benefits in preventing tooth decay, its impact on infants, "
         "especially regarding the appropriate dosage and potential risks, warrants careful consideration. "
         "In this blog post, we'll delve into scientific findings, health guidelines, and expert opinions "
         "to provide a comprehensive overview of fluoride's impact on infants.")

scientific_findings = "Scientific studies reveal ..."  # Add summarized findings here
health_guidelines_summary = "According to health organizations like the CDC, WHO, and ADA, ..." # Add guideline details here
expert_opinions = "Experts such as pediatricians and dentists suggest ..." # Add collected opinions here

blog_post = f"""
# {blog_title}

## Introduction
{intro}

## Scientific Findings
{scientific_findings}

## Health Guidelines
{health_guidelines_summary}

## Expert Opinions
{expert_opinions}

## Conclusion
In conclusion, fluoride plays a crucial role in preventing dental caries, but its use in infants should be carefully monitored to balance benefits and risks. Understanding the appropriate guidelines and consulting healthcare providers can help parents make informed decisions about fluoride use for their infants. By adhering to expert recommendations and health organization guidelines, parents can ensure their infants receive the dental benefits of fluoride without the associated risks of overexposure.
"""

print(blog_post)