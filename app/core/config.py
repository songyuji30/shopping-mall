import os

class settings:
  # API_V1_STR: str = "/api/v1"

  def get_database_url():
    if os.getenv("ENVIRONMENT", "local") == "test":
      return "sqlite:///./test.db"
    else:
      return "postgresql://default:ta0Jv4WNjgGU@ep-holy-star-a1wqb1c2.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
