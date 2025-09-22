"use client"

import { useState } from "react"
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Copy, Check, ExternalLink } from "lucide-react"

interface PermalinkModalProps {
  isOpen: boolean
  onClose: () => void
  permalink: string | null
}

export function PermalinkModal({ isOpen, onClose, permalink }: PermalinkModalProps) {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = async () => {
    if (!permalink) return

    try {
      await navigator.clipboard.writeText(permalink)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (error) {
      console.error("Failed to copy:", error)
    }
  }

  const openInNewTab = () => {
    if (permalink) {
      window.open(permalink, "_blank")
    }
  }

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Check className="h-5 w-5 text-green-500" />
            Upload Successful!
          </DialogTitle>
        </DialogHeader>

        <div className="space-y-4">
          <p className="text-sm text-muted-foreground">
            Your file has been uploaded successfully. Here's your permalink:
          </p>

          <div className="flex gap-2">
            <Input value={permalink || ""} readOnly className="flex-1" />
            <Button variant="outline" size="icon" onClick={copyToClipboard} className="shrink-0 bg-transparent">
              {copied ? <Check className="h-4 w-4 text-green-500" /> : <Copy className="h-4 w-4" />}
            </Button>
            <Button variant="outline" size="icon" onClick={openInNewTab} className="shrink-0 bg-transparent">
              <ExternalLink className="h-4 w-4" />
            </Button>
          </div>

          <div className="flex gap-2 pt-2">
            <Button onClick={copyToClipboard} className="flex-1">
              {copied ? "Copied!" : "Copy Link"}
            </Button>
            <Button variant="outline" onClick={onClose}>
              Close
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  )
}
