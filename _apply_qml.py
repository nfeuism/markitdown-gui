import re

# Map of English string → translation key (the new QML-specific ones)
qml_map = {
    # Sidebar
    '"MarkItDown GUI"': 'app.t("window_title")',
    '"MarkItDown"': 'app.t("sidebar_brand")',
    '"Document studio"': 'app.t("sidebar_subtitle")',
    '"Workspace"': 'app.t("sidebar_workspace")',
    '"Convert to Markdown"': 'app.t("sidebar_workspace_desc")',
    '"Add files, paste a URL, review Markdown, then export."': 'app.t("sidebar_tagline")',
    '"Help"': 'app.t("sidebar_help")',
    '"Settings"': 'app.t("sidebar_settings")',
    '"Convert documents and webpages"': 'app.t("sidebar_tooltip_workspace")',
    
    # Header
    '"Documents"': 'app.t("header_home_title")',
    '"Convert"': 'app.t("header_home_queue")',
    '"Conversion Complete!"': 'app.t("header_home_results")',
    '"Start new"': 'app.t("btn_start_new")',
    '"Quick access to updates, shortcuts, project links, and OCR resources."': 'app.t("header_help_detail")',
    
    # Sections
    '"FILES"': 'app.t("section_files")',
    '"DONE"': 'app.t("section_done")',
    '"SAVE"': 'app.t("section_save")',
    '"Output"': 'app.t("section_output")',
    '"Appearance"': 'app.t("section_appearance")',
    
    # Labels
    '"Default folder"': 'app.t("label_default_folder")',
    '"Batch size"': 'app.t("label_batch_size")',
    '"Theme"': 'app.t("label_theme")',
    '"Mode"': 'app.t("label_mode")',
    '"Ollama host"': 'app.t("label_ollama_host")',
    '"Port"': 'app.t("label_port")',
    '"Model"': 'app.t("label_model")',
    '"SDK server endpoint"': 'app.t("label_sdk_server_endpoint")',
    '"Endpoint"': 'app.t("label_endpoint")',
    '"Timeout"': 'app.t("label_timeout")',
    '"API key environment variable"': 'app.t("label_api_key_env")',
    '"Primary provider"': 'app.t("label_primary_provider")',
    '"Fallback provider"': 'app.t("label_fallback_provider")',
    '"Provider capabilities"': 'app.t("label_provider_capabilities")',
    '"Setup actions"': 'app.t("label_setup_actions")',
    '"OCR presets"': 'app.t("label_ocr_presets")',
    '"Settings profile"': 'app.t("label_settings_profile")',
    '"Common tasks"': 'app.t("label_common_tasks")',
    '"Add documents"': 'app.t("label_add_documents")',
    '"Convert a webpage"': 'app.t("label_convert_webpage")',
    '"Use OCR only when needed"': 'app.t("label_ocr_when_needed")',
    
    # Buttons
    '"Clear"': 'app.t("btn_clear")',
    '"Remove"': 'app.t("btn_remove")',
    '"Resume"': 'app.t("btn_resume")',
    '"Pause"': 'app.t("btn_pause")',
    '"Cancel"': 'app.t("btn_cancel")',
    '"Retry"': 'app.t("btn_retry")',
    '"Copy"': 'app.t("btn_copy")',
    '"Copy details"': 'app.t("btn_copy_details")',
    '"Save"': 'app.t("btn_save")',
    '"Browse"': 'app.t("btn_browse")',
    '"Export"': 'app.t("btn_export")',
    '"Import"': 'app.t("btn_import")',
    '"Open"': 'app.t("btn_open")',
    '"Dismiss"': 'app.t("btn_dismiss")',
    '"Back to queue"': 'app.t("btn_back_to_queue")',
    '"Retry failed"': 'app.t("btn_retry_failed")',
    '"Apply"': 'app.t("btn_apply")',
    '"Set folder"': 'app.t("btn_set_folder")',
    '"Choose files"': 'app.t("btn_choose_files")',
    '"Add files"': 'app.t("btn_add_files")',
    '"Add webpage"': 'app.t("btn_add_webpage")',
    '"Check for updates"': 'app.t("btn_check_updates")',
    '"Restart app"': 'app.t("btn_restart_app")',
    '"Copy command"': 'app.t("btn_copy_command")',
    '"Open logs"': 'app.t("btn_open_logs")',
    '"Copy diagnostics"': 'app.t("btn_copy_diagnostics")',
    '"Export bundle"': 'app.t("btn_export_bundle")',
    '"Open backup folder"': 'app.t("btn_open_backup")',
    '"Validate OCR"': 'app.t("btn_validate_ocr")',
    '"Test connection"': 'app.t("btn_test_connection")',
    '"Don\'t notify"': 'app.t("btn_dont_notify")',
    
    # Titles
    '"Combined save mode"': 'app.t("title_combined_save")',
    '"Prefer source folder"': 'app.t("title_prefer_source")',
    '"Save combined Markdown"': 'app.t("title_save_combined")',
    '"Save separate Markdown files"': 'app.t("title_save_separate")',
    '"Choose output folder"': 'app.t("title_choose_output")',
    '"Export settings profile"': 'app.t("title_export_profile")',
    '"Import settings profile"': 'app.t("title_import_profile")',
    '"Markdown review"': 'app.t("title_markdown_review")',
    '"Converted files"': 'app.t("title_converted_files")',
    '"Converting"': 'app.t("title_converting")',
    '"HTTP OCR"': 'app.t("title_http_ocr")',
    
    # Links
    '"Repository"': 'app.t("label_repository")',
    '"Releases"': 'app.t("label_releases")',
    '"Tesseract"': 'app.t("label_tesseract_install")',
    
    # Empty state
    '"Start with files or a webpage"': 'app.t("empty_start_message")',
    '"Drop files anywhere in this window, choose files from your system, or paste a URL."': 'app.t("empty_drop_hint")',
    '"Preview after conversion"': 'app.t("preview_after_conversion")',
    '"Check required provider settings before starting a batch."': 'app.t("ocr_check_required")',
    '"Profiles include provider endpoints and env var names, but exclude recent files, recent outputs, window state, and default output folders."': 'app.t("profiles_disclaimer")',
}

with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\qml\Main.qml", "r", encoding="utf-8") as f:
    qml = f.read()

count = 0
for old, new in qml_map.items():
    if old in qml:
        qml = qml.replace(old, new)
        count += 1
        print(f"  ✓ {old[:50]}...")

# Handle special case: window title
qml = qml.replace('title: "MarkItDown GUI"', 'title: app.t("window_title")')

with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\qml\Main.qml", "w", encoding="utf-8") as f:
    f.write(qml)

print(f"\nTotal replacements: {count}")
