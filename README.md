#  Agentic AI System for Multi-Step Tasks

An **Agent-based AI system** that processes complex tasks by breaking them into steps and assigning them to specialized agents.

##  Overview

This project implements a modular AI pipeline:

**Retriever → Analyzer → Writer**

It uses **async execution + RAG (FAISS)** to process documents and generate structured outputs.

## Video Demo
 https://drive.google.com/file/d/17VFMHoLYmJJYTtMhyGP4eB3FKfW_7mJg/view?usp=sharing

##  Architecture Diagram
https://drive.google.com/file/d/1DdPE5C5HjODOSUboyKgHieAM6CfqCJ6c/view?usp=sharing

## Pipeline Flow Diagram
https://drive.google.com/file/d/1MKzz7gcuGyptOUsH2TFuOor0WnbXPvsZ/view?usp=sharing

## Features
Agent-based architecture
Async pipeline with streaming
Message queue using Redis (with fallback)
Semantic search using FAISS
Structured output (Summary, Insights, Conclusion)
Retry & failure handling

## How It Works
Upload document
Text → chunks → embeddings
Stored in FAISS
Task flows through queue:
Retriever → fetch data
Analyzer → extract insights
Writer → generate report

## Tech Stack

Python • FastAPI • FAISS • Sentence Transformers • AsyncIO • Redis

## Limitations
Rule-based analyzer (not fully intelligent)
Local system (not distributed)

## Future Scope
LLM integration

Distributed queues (Kafka/RabbitMQ)

Frontend UI


