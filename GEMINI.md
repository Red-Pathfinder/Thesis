# Project Rules: Digital Pathology Thesis

These rules apply specifically to this thesis workspace and govern continuous ledger automation, Colab workflows, and decision export.

---

## 1. Automatic Memory & Decision Ledger Maintenance

**Do not wait for the user to ask for `.memory/` updates.**
Whenever any of the following events occur during a turn, you must **automatically** update the corresponding ledger file in `.memory/`:

1. **New Architectural Decision:** When introducing a new model backbone, loss function, optimizer setting, or data processing step $\rightarrow$ append a new node `[DEC-XXX]` to `.memory/DECISION_GRAPH.md` with context, rationale, and rejected alternatives. Update the Mermaid diagram.
2. **System State Change:** When components, dependencies, dataset paths, or contracts change $\rightarrow$ update `.memory/SYSTEM_STATE.md`.
3. **Experiment / Iteration Run:** When setting up, executing, or logging an experimental cycle or benchmark $\rightarrow$ append a log entry to `.memory/ITERATIONS.md`.

---

## 2. Instant Decision Export Trigger

Whenever the user asks to **"export decision"**, **"export decisions"**, **"create decision zip"**, or **"bundle decisions"**:
1. Run the bundle script immediately:
   ```bash
   python3 scripts/export_decisions_bundle.py
   ```
2. Report the generated ZIP file path so the user can drag-and-drop it directly into Claude.
3. Provide a brief 3-bullet recap of the latest decision nodes included in the bundle.

---

## 3. Git Synchronization Hygiene

* After completing a coherent unit of work (e.g., implementing a new dataset loader, adding a model module, or updating decision nodes), automatically commit with a descriptive conventional commit message (`feat:`, `fix:`, `docs:`, `refactor:`).
* Always check `git status` to ensure large model weights (`*.pt`) or raw images are never accidentally staged.
