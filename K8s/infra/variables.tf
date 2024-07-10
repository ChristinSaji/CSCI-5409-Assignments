variable "gcp_svc_key" {
  description = "Path to the GCP service account key file"
}

variable "gcp_project" {
  description = "GCP project ID"
}

variable "gcp_region" {
  description = "GCP region"
}

variable "gcp_zone" {
  description = "GCP zone"
}

variable "persistent_disk_size" {
  default     = 10
  description = "Disk size (in GB) for the persistent disk"
}

variable "gke_image_type" {
  default     = "COS_CONTAINERD"
  description = "Image type for the GKE nodes"
}

variable "gke_machine_type" {
  default     = "e2-small"
  description = "Machine type for the GKE nodes"
}

variable "gke_disk_size" {
  default     = 20
  description = "Disk size (in GB) for the GKE nodes"
}

variable "gke_disk_type" {
  default     = "pd-standard"
  description = "Disk type for the GKE nodes"
}

variable "gke_num_nodes" {
  default     = 1
  description = "Number of nodes in the GKE node pool"
}
