import uvicorn

from app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app, port=5004, log_level="debug"
    )  # pyright: reportGeneralTypeIssues=false
