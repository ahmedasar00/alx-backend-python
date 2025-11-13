# Django Signals, ORM & Advanced ORM Techniques

**Weight:** 1  
**Project Duration:** Sep 29, 2025 – Oct 6, 2025  
**Manual QA Review:** Pending  
**Auto QA Review:** 0.0/19 mandatory  
**Final Score:** Waiting for reviews

---

## Overview

Modern web applications require performance, modularity, and clean architecture. Django provides powerful tools that help developers build maintainable and efficient backends. This project focuses on three key concepts:

- **Event Listeners using Django Signals**  
  Signals allow decoupled parts of your application to communicate by emitting and listening to events — for example, sending confirmation emails or logging actions when a model instance is saved or deleted.

- **Django ORM & Advanced ORM Techniques**  
  Django’s ORM allows you to interact with your database using Python instead of raw SQL. It includes advanced performance tools like `select_related`, `prefetch_related`, and annotations to optimize queries and avoid common issues like the N+1 problem.

- **Basic Caching**  
  Caching stores frequently accessed data to improve response times and reduce database load. Django supports multiple levels of caching, such as view-level, template fragment, and low-level caching.

Together, these features improve performance, scalability, and maintainability in Django backend systems.

---

## Learning Objectives

By completing this project, you’ll learn how to:

- Use **Django Signals** to create event-driven features.
- Perform CRUD operations using **Django ORM**.
- Apply **advanced ORM techniques** for better query performance.
- Implement **basic caching strategies** to improve speed and efficiency.
- Write clean, decoupled, and testable backend code.

---

## Learning Outcomes

After completing this module, you will be able to:

- Decouple side effects from core logic using **signals**.
- Efficiently manipulate and retrieve data using **Django ORM**.
- Optimize queries to prevent performance bottlenecks.
- Use caching to reduce server workload and response time.
- Maintain a clean, modular, and performant backend structure.

---

## 1. Event Listeners Using Django Signals

### What Are Signals?

Signals allow certain senders to notify receivers when specific actions occur, such as saving or deleting a model instance.

### Common Signals

- `pre_save` / `post_save`
- `pre_delete` / `post_delete`
- `m2m_changed`
- `request_started` / `request_finished`

### Best Practices

- Keep signal handlers short and efficient.
- Use the `@receiver` decorator for clarity.
- Separate core logic from signal handlers by using services or utilities.
- Disconnect signals during tests to avoid side effects.

---

## 2. Django ORM Basics

### What Is ORM?

The **Object-Relational Mapper** lets you interact with the database using Python classes and methods instead of raw SQL.

### Common Operations

- **Create:** `Model.objects.create(...)`
- **Retrieve:** `Model.objects.get()`, `.filter()`, `.all()`
- **Update:** `.save()`, `.update()`
- **Delete:** `.delete()`

### Best Practices

- Handle exceptions (`DoesNotExist`, `MultipleObjectsReturned`).
- Use filters instead of fetching all records.
- Validate data before saving.

---

## 3. Advanced ORM Techniques

### Tools for Performance

- `select_related()` – Optimize foreign key lookups.
- `prefetch_related()` – Optimize many-to-many and reverse lookups.
- `annotate()` – Perform aggregations (count, sum, etc.).
- `Q()` and `F()` – Create complex queries and field-based operations.
- **Custom Managers** – Encapsulate reusable query logic.

### Best Practices

- Avoid redundant queries with eager loading.
- Use `only()` or `defer()` to load specific fields.
- Profile queries using Django Debug Toolbar or `.query`.

---

## 4. Basic Caching in Django

### What Is Caching?

Caching saves the results of expensive operations to improve performance. Django supports multiple caching levels.

### Common Tools

- `@cache_page(60 * 15)` – Cache entire views.
- `{% cache 300 "sidebar" %}` – Cache template fragments.
- `cache.set()` / `cache.get()` – Manual low-level caching.

### Best Practices

- Avoid caching sensitive or user-specific data.
- Use versioned and descriptive cache keys.
- Invalidate cache when data changes.

---

## 🧩 Tasks

### 0. Implement Signals for User Notifications

**Goal:** Automatically notify users when they receive a new message.

- Create a `Message` model (`sender`, `receiver`, `content`, `timestamp`).
- Use `post_save` signal to create a `Notification` for the receiver.
- Store notifications in a `Notification` model linked to `User` and `Message`.

📁 **Files:**  
`messaging/models.py`, `messaging/signals.py`, `messaging/apps.py`, `messaging/admin.py`, `messaging/tests.py`

---

### 1. Create a Signal for Logging Message Edits

**Goal:** Log and save old message content before edits.

- Add an `edited` field to the `Message` model.
- Use `pre_save` to log old content into a `MessageHistory` model.
- Display edit history in the UI.

📁 **Files:**  
`messaging/models.py`

---

### 2. Use Signals for Deleting User-Related Data

**Goal:** Clean up related data when a user deletes their account.

- Create a `delete_user` view.
- Use `post_delete` on the `User` model to delete messages, notifications, and histories.
- Ensure database integrity using `CASCADE` or custom signal logic.

📁 **Files:**  
`messaging/views.py`

---

### 3. Leverage Advanced ORM Techniques for Threaded Conversations

**Goal:** Implement threaded replies and optimize data retrieval.

- Add `parent_message` (self-referential FK) to the `Message` model.
- Use `select_related` and `prefetch_related` to reduce queries.
- Implement recursive queries to fetch full message threads.

📁 **Files:**  
`messaging/models.py`

---

### 4. Custom ORM Manager for Unread Messages

**Goal:** Create a manager to filter unread messages.

- Add a `read` boolean field to `Message`.
- Create `UnreadMessagesManager` to return unread messages for a user.
- Use `.only()` to load minimal fields for performance.

📁 **Files:**  
`messaging/models.py`

---

### 5. Implement Basic View Cache

**Goal:** Add caching to improve performance in message views.

- Configure cache in `settings.py`:.

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```
