FROM gcc:13.2.0-alpine

# Crée un utilisateur non-root
RUN adduser -D grader

# Dossier de travail
WORKDIR /home/grader/work

# Copier le script d’entrée
COPY entrypoint.sh /usr/local/bin/run_test.sh
RUN chmod +x /usr/local/bin/run_test.sh

# Droits sur le dossier de travail
RUN chown grader:grader /home/grader/work

USER grader

ENTRYPOINT ["/usr/local/bin/run_test.sh"]
