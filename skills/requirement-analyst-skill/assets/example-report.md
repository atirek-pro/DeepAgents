# Requirements Analysis

## Confirmed Facts
- Requirement title: "User Profile File Upload".
- Users shall be able to upload files to their profile (mandatory: "shall").
- Uploaded files should be stored securely (recommended: "should").
- The system should support common file types (recommended: "should").

## Ambiguities
- **"Users shall be able to upload files to their profile."**
  Reason: [Business] "Users" does not say which roles or tiers may upload; "profile" is not defined (own profile only? shared or public?); no limit on number or total storage per user; replace, delete and download behaviour is not mentioned.
- **"Uploaded files should be stored securely."**
  Reason: [Security] "securely" has no standard (encryption at rest, access control, malware scanning, compliance); "should" does not say whether it is mandatory; retention and deletion rules are not stated.
- **"The system should support common file types."**
  Reason: [Technical] "common" is an unbounded set with no list of allowed or blocked types; no maximum file size; no validation or error behaviour for unsupported files.
- **(absent) no acceptance criteria or non-functional targets**
  Reason: [NFR] No upload performance, availability or success criteria, so the work cannot be tested as done.

## Clarification Questions
- Q1: Which user roles may upload, and are files visible only to the owner or to others?
- Q2: Which security controls are mandatory for stored files (encryption at rest, malware scanning, access control, compliance standard)?
- Q3: Which exact file types are allowed, and what is the maximum size per file?
- Q4: Is there a limit on the number of files or total storage per user?
- Q5: Can users replace, delete and download uploaded files, and how long are files retained after account deletion?
- Q6: What should the user see when an upload fails or a file type is rejected?
- Q7: What are the acceptance criteria and expected upload performance?

## Assumptions
- (Q1) Only authenticated users can upload, and files are private to the owning user.
- (Q2) Files are encrypted at rest, scanned for malware, and served only to the owner via authorised access.
- (Q3) Allowed types are JPG, PNG, PDF, DOCX; maximum 10 MB per file.
- (Q4) Maximum 20 files and 100 MB per user.
- (Q5) Users can replace, delete and download their files; files are deleted when the account is deleted.
- (Q6) The user sees a clear error message naming the reason, and nothing is stored.
- (Q7) Acceptance is a successful upload and retrieval of an allowed file within a normal request time (about 5 s for 10 MB).

## Summary
The requirement asks for authenticated profile file upload with secure storage and support for common file types. It is mandatory in intent but vague on roles, security controls, file types, limits and failure behaviour. Verdict: Ready with assumptions only after the seven questions are confirmed.
