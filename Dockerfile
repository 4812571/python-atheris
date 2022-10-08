FROM fuzzers/atheris:2.0.7-python3.9
COPY src/mayhemit.py /mayhemit.py

# Change Permissions
RUN chmod +x /mayhemit.py

# Set to fuzz!
ENTRYPOINT []
CMD ["/mayhemit.py"]