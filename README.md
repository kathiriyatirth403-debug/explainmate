\# 🤖 ExplainMate — your friendly code explainer



Paste any code snippet and ExplainMate explains what it does in plain,

beginner-friendly English — like a kind senior sitting next to you.

Every answer ends with a \*\*Confidence Meter\*\* and an encouraging line. 🚀



Built for the AWS Builder Center "Build an Agent" Weekend Challenge (Oct 2026).



\## Live Demo

🌐 https://d3sc54xewx0g5m.cloudfront.net



\## Architecture

User → CloudFront (HTTPS) → S3 (web UI)

User → API Gateway (HTTP API) → AWS Lambda (Python 3.12) → Amazon Bedrock (Nova Micro)



\## AWS Services Used

\- Amazon Bedrock (Nova Micro) — the explanation model

\- AWS Lambda — serverless agent logic

\- Amazon API Gateway — public HTTPS endpoint

\- Amazon S3 — static website hosting

\- Amazon CloudFront — HTTPS delivery

\- AWS IAM — least-privilege role



\## The Delightful Detail

A \*\*Confidence Meter\*\* (clarity %) + an encouraging closing line turns a

cold tool into a buddy. Friendly error messages carry the same warmth.



\## License

MIT

