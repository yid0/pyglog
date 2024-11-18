LOG_LEVEL ?=info
LOG_FORMAT ?=standard

.PHONY:	install
install:
	pip install -r requirements.txt  --root-user-action

.PHONY:	log-info-standard
log-info-standard:
	LOG_LEVEL=info LOG_FORMAT=standard python main.py

.PHONY:	log-info-ecs
log-info-ecs:
	LOG_LEVEL=info LOG_FORMAT=ecs python main.py

.PHONY:	log-info
log-info:
	make log-info-standard && \
	make log-info-ecs

.PHONY:	log-error-standard
log-error-standard:
	LOG_LEVEL=error LOG_FORMAT=standard python main.py

.PHONY:	log-fatal-ecs
log-fatal-ecs:
	LOG_LEVEL=fatal LOG_FORMAT=ecs python main.py

.PHONY:	log-error-ops
log-error-ops:
	LOG_LEVEL=error LOG_FORMAT=opensearch python main.py