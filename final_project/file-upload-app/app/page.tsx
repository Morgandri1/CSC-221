"use client"

import { useState } from "react"
import { FileUpload } from "@/components/file-upload"
import { PermalinkModal } from "@/components/permalink-modal"

export default function HomePage() {
  const [permalink, setPermalink] = useState<string | null>(null)
  const [isModalOpen, setIsModalOpen] = useState(false)

  const handleUploadSuccess = (url: string) => {
    setPermalink(url)
    setIsModalOpen(true)
  }

  const handleCloseModal = () => {
    setIsModalOpen(false)
    setPermalink(null)
  }

  return (
    <main className="min-h-screen bg-background flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-2">File Upload</h1>
          <p className="text-muted-foreground">Upload your files and get a shareable permalink</p>
        </div>

        <FileUpload onUploadSuccess={handleUploadSuccess} />

        <PermalinkModal isOpen={isModalOpen} onClose={handleCloseModal} permalink={permalink} />
      </div>
    </main>
  )
}
