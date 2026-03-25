# AI-Based Fitness Coaching Assistant

This repository folder supports a **four-phase** intelligent coaching system: prediction models plus LLM explanations, unified later behind a single API. **Work is currently focused on Phase 1 only**; Phases 2–4 are planned, not implemented here yet.

---

## Roadmap (four phases)

| Phase | Name | Goal | Status |
|------:|------|------|--------|
| **1** | **Weight adjustment prediction** | Predict **delta weight** for the next session from performance signals; pair with **LLM explanation** (coach-facing output: `delta_weight`, `unit`, `confidence`, `explanation`). | **In progress** — data pipeline, labels, and supporting features (e.g. RPE) are being built. |
| **2** | **Fatigue detection** | Infer fatigue level from load, RPE trends, volume, frequency; LLM explains the label. | Planned |
| **3** | **Plateau detection** | Trend analysis over sessions (weight/reps progression, stability); detect stagnation; LLM suggests adjustments. | Planned |
| **4** | **API integration** | Single REST API routing inputs to all models and returning recommendations + explanations. | Planned |

The scripts in this folder are **Phase 1 enablers**: they do **not** constitute the finished weight-delta model or the full product.

---

## Where we are now: Phase 1 (in progress)

Phase 1 still needs a trained **delta-weight** model and the final coach API contract. So far, this folder delivers:

- **Cleaned datasets** aligned for modeling (`workouts_cleaned.csv`, `weightlifting_cleaned.csv`).
- **Rule-based `success`** on the weightlifting side (for future features / labels).
- **Auxiliary RPE prediction**: multiple regressors are benchmarked on limited labeled data to **impute RPE** where missing — this supports richer Phase 1 inputs, not the final deliverable of the project.

**Not done yet (Phase 1):**

- Session-paired labels: `(weight, sets, reps, rpe, success) → delta_weight`.
- Trained production model for `delta_weight` + calibrated `confidence`.
- LLM layer grounded on model outputs and session context.
- Persistence, validation, and deployment hooks for the weight model.

---

## Phase 1 target (reminder)

- **Inputs (conceptual):** current load, sets, reps, RPE, success (and optionally short history).
- **Output (coach contract):** `delta_weight`, `unit`, `confidence`, `explanation` (LLM).

---

## Phases 2–3 (planned, not in this codebase yet)

- **Phase 2 — Fatigue:** features from volume change, RPE, performance variance, weekly frequency → fatigue level + evidence-style summary for the LLM.
- **Phase 3 — Plateau:** time-series features across sessions → plateau vs no plateau + trend indicators + LLM narrative.

---

## Phase 4 (planned)

- One **REST API** that accepts client payloads, runs the relevant models, and returns structured predictions plus LLM explanations.

---

## Files in this folder (Phase 1 groundwork)

| File | Role |
|------|------|
| `workouts.csv` | Source: `weight_kg`, `reps`, `rpe`. |
| `weightlifting_workouts.csv` | Source: session keys, `Set Order`, `Weight`, `Reps`. |
| `prepare_workout_csvs.py` | Builds `workouts_cleaned.csv` and `weightlifting_cleaned.csv`; converts lb→kg; adds `sets` and session-order-based `success` on export. |
| `add_success_labels.py` | Optional: recomputes `success` on `weightlifting_cleaned.csv` using median reps per `(weight, sets)`. |
| `predict_rpe.py` | Benchmarks regressors for RPE; picks best by **MAE**; writes predicted `rpe` into `weightlifting_cleaned.csv`. |
| `schema.json` | Draft contract for the **weight** model output (coach-facing). |

### Cleaned schemas (current)

- `workouts_cleaned.csv`: `weight`, `reps`, `rpe`
- `weightlifting_cleaned.csv`: `weight`, `reps`, `sets`, `success`, `rpe` (after `predict_rpe.py`)

---

## Success label (current helper logic)

`add_success_labels.py`:

1. Group by `weight` and `sets`.
2. `expected_reps` = median reps in that group.
3. `success = 1` if `reps >= expected_reps`, else `0`.

---

## RPE benchmarking (auxiliary to Phase 1)

- Models: Linear, Ridge, Lasso, RandomForest, GradientBoosting, KNN (scaled).
- Metrics: **MAE** (primary), **RMSE** (secondary). `R²` was dropped because training RPE is almost constant in places.

**Limitation:** mostly `RPE ≈ 10` in training data → predictions are bootstrap estimates until labels diversify.

---

## How to run (Phase 1 pipeline scripts)

From `weight_change_prediction_model`:

1. `python prepare_workout_csvs.py`
2. (Optional) `python add_success_labels.py`
3. `python predict_rpe.py`

---

## Suggested next steps (Phase 1)

- Build **delta_weight** labels by pairing consecutive sessions per exercise.
- Train and evaluate a **delta_weight** regressor (or policy + uncertainty).
- Add `rpe_source` and avoid overwriting raw CSVs with predictions.
- Save models with `joblib` for later Phase 4 API.

---

## Suggested next steps (later phases)

- Phase 2/3: separate feature builders and model modules; shared schemas.
- Phase 4: FastAPI (or similar) service wrapping all endpoints.
