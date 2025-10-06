"use client"

import { useState, useCallback } from "react"
import { useDropzone } from "react-dropzone"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Upload, File, Loader2 } from "lucide-react"
import { cn } from "@/lib/utils"
import Axios from "axios";

interface FileUploadProps {
  onUploadSuccess: (url: string) => void
}

export function FileUpload({ onUploadSuccess }: FileUploadProps) {
  const [isUploading, setIsUploading] = useState(false)
  const [uploadError, setUploadError] = useState<string | null>(null)

  const uploadFile = async (file: File) => {
    setIsUploading(true)
    setUploadError(null)

    try {
      // Get the server URL from environment or use localhost as fallback
      const serverUrl = "https://csc-221-production.up.railway.app"

      let formdata = new FormData()
      formdata.append("file", file)
      console.log(file)
      console.log(formdata)
      
      const response = await Axios(`${serverUrl}/upload`, {
        method: "POST",
        data: formdata,
        headers: {
          "Content-Type": "multipart/form-data",
          "Authorization": process.env.APP_SECRET || "f461396e28955e716a7625901cc43ccd"
        },
      })

      if (response.status !== 200) {
        throw new Error(`Request failed: ${response.statusText}`)
      }

      // Assume the server returns the permalink URL
      const result = response.data
      if (result.status == 1) {
        setUploadError("Failed to upload! " + result.error)
        setIsUploading(false)
        return
      }
      const permalink = result.filename ? `${serverUrl}/get/${result.filename}` : `${serverUrl}/get/${encodeURIComponent(file.name)}`

      onUploadSuccess(permalink)
    } catch (error) {
      console.error("Upload error:", error)
      setUploadError(error instanceof Error ? error.message : "Upload failed")
    } finally {
      setIsUploading(false)
    }
  }

  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      uploadFile(acceptedFiles[0])
    }
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    multiple: false,
    disabled: isUploading,
  })

  return (
    <Card className="p-8">
      <div
        {...getRootProps()}
        className={cn(
          "border-2 border-dashed rounded-lg p-12 text-center cursor-pointer transition-colors",
          isDragActive ? "border-primary bg-primary/5" : "border-border hover:border-primary/50",
          isUploading && "cursor-not-allowed opacity-50",
        )}
      >
        <input {...getInputProps()} />

        <div className="flex flex-col items-center gap-4">
          {isUploading ? (
            <Loader2 className="h-12 w-12 text-primary animate-spin" />
          ) : (
            <Upload className="h-12 w-12 text-muted-foreground" />
          )}

          <div className="space-y-2">
            {isUploading ? (
              <p className="text-lg font-medium">Uploading...</p>
            ) : isDragActive ? (
              <p className="text-lg font-medium">Drop your file here</p>
            ) : (
              <>
                <p className="text-lg font-medium">Drag & drop a file here</p>
                <p className="text-sm text-muted-foreground">or click to select a file</p>
              </>
            )}
          </div>

          {!isUploading && (
            <Button variant="outline" className="mt-2 bg-transparent">
              <File className="h-4 w-4 mr-2" />
              Choose File
            </Button>
          )}
        </div>
      </div>

      {uploadError && (
        <div className="mt-4 p-3 bg-destructive/10 border border-destructive/20 rounded-md">
          <p className="text-sm text-destructive">{uploadError}</p>
        </div>
      )}
    </Card>
  )
}
