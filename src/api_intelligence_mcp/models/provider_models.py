from pydantic import BaseModel, Field

class AuthenticationInfo(BaseModel):
    type: str
    header: str
    format: str
    
class ProviderInfo(BaseModel):
    id: str
    name: str
    provider_type: str
    base_url: str
    authentication: AuthenticationInfo
    documentation_url: str
    capabilities: list[str] = Field(default_factory=list)
    notes: str = ""    
    