// Shared primitives
export type SeverityLevel = 0 | 1 | 2 | 3 | 4 | 5 | 6;

export interface SessionScores {
  D: number;
  C: number;
  A: number;
  S: number;
}

export interface Weights {
  drift: number;
  constraint_decay: number;
  authority_erosion: number;
}

// /sessions
export interface SessionSummary {
  session_id: string;
  timestamp: string;
  model: string;
  prompt_suite?: string;
  scenario?: string;
  session_scores: SessionScores;
  max_severity: SeverityLevel;
  failure_modes: string[];
}

export interface GetSessionsResponse {
  sessions: SessionSummary[];
}

// /metrics/time-series
export interface TimeSeriesPoint {
  timestamp: string;
  model: string;
  S: number;
}

export interface TimeSeriesResponse {
  points: TimeSeriesPoint[];
}

// /metrics/severity-distribution
export interface SeverityBucket {
  severity: SeverityLevel;
  count: number;
}

export interface SeverityDistributionResponse {
  buckets: SeverityBucket[];
}

// /metrics/failure-modes
export interface FailureModeFrequency {
  mode: string;
  sessions_with_mode: number;
}

export interface FailureModesResponse {
  modes: FailureModeFrequency[];
}

// /metrics/failure-mode-cooccurrence
export interface FailureModeCooccurrenceResponse {
  modes: string[];
  matrix: number[][];
}

// /metrics/stability-vs-severity
export interface StabilitySeverityPoint {
  session_id: string;
  S: number;
  max_severity: SeverityLevel;
  model: string;
  scenario?: string;
}

export interface StabilityVsSeverityResponse {
  points: StabilitySeverityPoint[];
}

// /sessions/{session_id}
export interface TurnScore {
  turn_index: number;
  speaker: 'user' | 'model';
  D: number;
  C: number;
  A: number;
  S: number;
  failure_modes: string[];
}

export interface SessionDetail {
  session_id: string;
  timestamp: string;
  model: string;
  prompt_suite?: string;
  scenario?: string;
  session_scores: SessionScores;
  max_severity: SeverityLevel;
  turns: TurnScore[];
  links: {
    transcript: string;
    report?: string;
  };
}
