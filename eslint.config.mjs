import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: [".tmp/**", "docs/**", "reports/**", "memoires/**", "research_notes/**", "**/*.md"] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ["**/*.ts", "**/*.tsx"],
    rules: {
      "max-lines-per-function": ["error", { max: 10, skipBlankLines: true, skipComments: true }],
      "no-inline-comments": "error",
    },
  },
);
