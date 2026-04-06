# Report: AI-Assisted Sales Follow-Up Email Generation

## Business Use Case

The workflow focuses on automating the drafting of post-meeting sales follow-up emails. In many sales teams, representatives spend significant time summarizing meetings, writing emails, and ensuring alignment with customer needs. This task is repetitive but important, as it directly affects customer relationships and conversion rates.

The system takes structured or semi-structured meeting notes as input (e.g., customer name, company, discussion points, and goals) and generates a professional follow-up email. Automating this process can improve efficiency, reduce manual workload, and ensure consistent communication quality across teams.

---

## Model Choice and Observations

I used the **Gemini 2.0 Flash model** for this prototype due to its free-tier availability and fast response time. It is suitable for lightweight text generation tasks such as email drafting.

During development, I also considered using OpenAI models. However, Gemini was selected primarily for accessibility. In practice, I observed that:

- Gemini performs well on structured prompts
- It occasionally struggles with rate limits on the free tier
- Without clear instructions, it may hallucinate details (e.g., pricing or product features)

Overall, the model is capable, but its performance depends heavily on prompt design and input quality.

---

## Baseline vs. Final Design Comparison

### Baseline (Initial Prompt)
The initial prompt was simple and broadly instructed the model to write a professional follow-up email based on meeting notes. While it produced readable outputs, it had several issues:
- Occasionally invented details not present in the input
- Output format was inconsistent
- Did not handle missing or ambiguous information well

### Final Design (After Iterations)
After two prompt revisions, the system improved significantly:
- Added strict rules to **only use provided information**
- Introduced a **structured output format** (subject, email body, review flag)
- Included **constraints to avoid hallucination**
- Added a **review flag mechanism** for risky or incomplete cases

### Improvement Summary
- **Improved:** factual accuracy, consistency, and safety
- **Stayed the same:** overall tone and readability
- **Tradeoff:** slightly more conservative language in emails

The prompt iteration process demonstrated that small changes in instructions can significantly improve output reliability.

---

## Limitations and Failure Cases

The prototype still has limitations:

- It cannot verify factual correctness beyond the provided input
- If the input is incomplete or ambiguous, the output may be too generic
- The model may still produce overly confident language in edge cases
- Free-tier API rate limits can affect reliability during testing

Because of these limitations, **human review is still required**, especially for:
- pricing discussions
- contractual commitments
- unclear or incomplete meeting notes

---

## Deployment Recommendation

I would recommend deploying this workflow **only with human-in-the-loop review**.

The system is valuable as a **drafting assistant**, not a fully autonomous solution. It can:
- save time
- standardize communication
- reduce repetitive writing tasks

However, it should not be used to send emails automatically without review, particularly in high-stakes or customer-facing scenarios.

Under the following conditions, deployment would be appropriate:
- outputs are reviewed before sending
- prompts are well-controlled and tested
- users are trained to provide structured inputs

---

## Conclusion

This prototype demonstrates that LLMs can effectively support business communication workflows. With proper prompt design and safeguards, the system can deliver meaningful productivity gains. However, reliability and accountability still require human oversight.