/**
 * Assignment 05 (TypeScript): single choice decision.
 *
 *   npm init -y && npm install openai
 *   OPENAI_API_KEY=sk-... npx tsx examples/decide_once.ts
 */

import OpenAI from "openai";

const client = new OpenAI();

const ticket =
  "Customer: I was charged twice for order #8821. Please refund the duplicate $49 charge.";

const decision = await client.decisions.create({
  model: "gpt-6-luna",
  input: ticket,
  questions: [
    {
      type: "choice",
      name: "department",
      instructions: "Which team should handle this message?",
      choices: [
        { value: "billing" },
        { value: "technical" },
        { value: "shipping" },
        { value: "other" },
      ],
    },
  ],
});

for (const answer of decision.answers) {
  console.log(JSON.stringify(answer, null, 2));
  if (answer.type === "choice") {
    console.log(`choice=${answer.choice} confidence=${answer.confidence}`);
  } else if (answer.type === "refusal") {
    console.error(`refusal for ${answer.name}`);
  }
}
