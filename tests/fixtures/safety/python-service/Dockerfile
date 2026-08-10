FROM python:3.11-slim AS builder

RUN python -m venv /opt/venv
COPY uvicorn/ /tmp/uvicorn/
RUN cp -R /tmp/uvicorn "$(/opt/venv/bin/python -c 'import site; print(site.getsitepackages()[0])')/"

FROM python:3.11-slim

RUN useradd --create-home --uid 1000 appuser
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
USER appuser
EXPOSE 8080
CMD ["python", "-m", "uvicorn"]
