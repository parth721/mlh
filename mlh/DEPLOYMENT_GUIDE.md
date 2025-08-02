# Kubernetes Deployment Guide with Persistent Storage

This guide explains how to deploy the MLH Django application with persistent database storage in Kubernetes.

## Overview of Changes Made

### 1. Persistent Volume Configuration (`storage.yml`)
- Changed storage class from `manual` to `standard` for better compatibility
- Updated access mode from `ReadWriteMany` to `ReadWriteOnce` (SQLite only needs single-writer)
- Increased storage from 500Mi to 1Gi
- Changed host path from `/tmp/data` to `/var/lib/mlh-data` for better persistence
- Added proper volume reclaim policy to retain data

### 2. Deployment Configuration (`deployment.yaml`)
- Fixed volume mount to mount directory `/usr/src/app/data` instead of the file directly
- This allows SQLite to create and manage the database file properly

### 3. Django Settings (`mlh/settings.py`)
- Updated database path to use the persistent volume: `/usr/src/app/data/db.sqlite3`
- This ensures the database file is stored in the persistent volume

### 4. Docker Configuration (`Dockerfile`)
- Updated working directory to `/usr/src/app` for consistency
- Added creation of data directory with proper permissions
- Added entrypoint script for proper database initialization

### 5. Database Initialization (`entrypoint.sh`)
- Added script to handle database migrations automatically
- Ensures database is created on first run
- Runs migrations on every startup to keep schema updated

## Deployment Steps

### Step 1: Apply Storage Configuration
```bash
kubectl apply -f storage.yml
```

### Step 2: Verify Persistent Volume
```bash
kubectl get pv sqlite-pv
kubectl get pvc sqlite-pvc
```

### Step 3: Deploy the Application
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Step 4: Verify Deployment
```bash
kubectl get pods
kubectl get services
kubectl logs -f deployment/mlh-deployment
```

## Key Benefits of This Configuration

1. **Data Persistence**: Database data survives pod restarts, deletions, and redeployments
2. **Automatic Initialization**: Database is automatically created and migrated on first run
3. **Proper File Permissions**: Ensures SQLite can read/write to the database file
4. **Scalable Storage**: Easy to increase storage size if needed
5. **Production Ready**: Uses standard storage class and proper volume mounting

## Important Notes

### For Production Environments:
- Consider using cloud-based persistent volumes (AWS EBS, GCP Persistent Disk, Azure Disk)
- Set up regular database backups
- Use secrets for sensitive configuration
- Consider using PostgreSQL or MySQL for better scalability

### Storage Classes:
- `standard`: Default storage class (recommended)
- `fast`: SSD-based storage (if available)
- Cloud providers have specific storage classes (gp2, pd-standard, etc.)

### Monitoring:
```bash
# Check persistent volume status
kubectl describe pv sqlite-pv

# Check persistent volume claim status
kubectl describe pvc sqlite-pvc

# Monitor pod logs
kubectl logs -f deployment/mlh-deployment

# Check database file in pod
kubectl exec -it deployment/mlh-deployment -- ls -la /usr/src/app/data/
```

## Troubleshooting

### If PVC is Pending:
1. Check if storage class exists: `kubectl get storageclass`
2. Verify node has sufficient disk space
3. Check PV and PVC are properly bound

### If Database Issues:
1. Check file permissions in the pod
2. Verify the data directory is mounted correctly
3. Check Django migrations are running properly

### Clean Deployment (if needed):
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete pvc sqlite-pvc
kubectl delete pv sqlite-pv
```

## File Structure After Deployment:
```
/usr/src/app/
├── data/                 # Persistent volume mount point
│   └── db.sqlite3       # SQLite database file (persistent)
├── manage.py
├── mlh/
├── frontend/
├── backend/
└── entrypoint.sh
```
