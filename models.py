from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class KeyDifference(BaseModel):
    aspect: str
    polymarket: str
    kalshi: str

class ArbitrageOpportunity(BaseModel):
    scenario: str

class EquivalenceSchema(BaseModel):
    relationship: Literal['direct','inverse']
    same_outcome_event: bool
    resolution_criteria_equivalent: bool
    key_differences: Optional[List[KeyDifference]] = None
    equivalence_rating: int = Field(ge=1, le=10)  # minimum=1, maximum=10
    arbitrage_opportunities: Optional[List[ArbitrageOpportunity]] = None
    detailed_reasoning: str

# Go game move response schema
class GoMoveResponse(BaseModel):
    move_type: Literal['coordinate', 'pass', 'resign'] = Field(..., description="Type of move being made")
    move: str = Field(..., description="The coordinate like 'D4', 'K10', or special move like 'PASS', 'RESIGN'")
    reasoning: str = Field(..., description="Brief explanation of the move choice")
    thinking: Optional[str] = Field(default="", description="Detailed step-by-step thinking process")
    confidence: Optional[int] = Field(default=None, ge=1, le=10, description="Confidence in this move (1-10)")