{{/* Reusable Deployment Template for Microservices */}}
{{- define "microservice.deployment" -}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .serviceName }}
  labels:
    app: {{ .serviceName }}
spec:
  replicas: {{ .config.replicaCount }}
  selector:
    matchLabels:
      app: {{ .serviceName }}
  template:
    metadata:
      labels:
        app: {{ .serviceName }}
    spec:
      containers:
        - name: {{ .serviceName }}
          image: "{{ .Values.global.registry }}/{{ .config.imageName }}:{{ .Values.global.imageTag }}"
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: {{ .config.internalPort }}
          env:
            - name: HOST_IP
              value: {{ .config.env.HOST_IP | quote }}
            - name: PORT
              value: {{ .config.internalPort | quote }}
          # Liveness and Readiness Probes ensure zero-downtime rolling updates
          livenessProbe:
            httpGet:
              path: /health
              port: {{ .config.internalPort }}
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .config.internalPort }}
            initialDelaySeconds: 5
            periodSeconds: 5
          resources:
            limits:
              cpu: 200m
              memory: 256Mi
            requests:
              cpu: 100m
              memory: 128Mi
---
apiVersion: v1
kind: Service
metadata:
  name: {{ .serviceName }}
  labels:
    app: {{ .serviceName }}
spec:
  type: ClusterIP
  ports:
    - port: {{ .config.internalPort }}
      targetPort: {{ .config.internalPort }}
      protocol: TCP
  selector:
    app: {{ .serviceName }}
{{- end -}}
