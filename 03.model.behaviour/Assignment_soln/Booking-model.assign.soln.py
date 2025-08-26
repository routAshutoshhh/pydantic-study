from pydantic import field_validator, BaseModel, Field, model_validator, computed_field

class BookingModel(BaseModel):
    user_id: str
    room_id: str
    nights: int = Field(...,ge=1)
    rates_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights*self.rates_per_night