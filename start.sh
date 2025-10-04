#!/bin/bash

# 🚀 BioSpaceSearch AI Platform - Quick Start Script

echo "🚀 Starting BioSpaceSearch AI Platform..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo -e "${YELLOW}⚠️  Node.js is not installed. Please install Node.js 18+ first.${NC}"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python 3 is not installed. Please install Python 3.10+ first.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Node.js $(node --version) found${NC}"
echo -e "${GREEN}✅ Python $(python3 --version) found${NC}"
echo ""

# Create .env if not exists
if [ ! -f .env ]; then
    echo -e "${BLUE}📝 Creating .env file...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ .env file created${NC}"
fi

# Install frontend dependencies
if [ ! -d "frontend/node_modules" ]; then
    echo -e "${BLUE}📦 Installing frontend dependencies...${NC}"
    cd frontend
    npm install
    cd ..
    echo -e "${GREEN}✅ Frontend dependencies installed${NC}"
else
    echo -e "${GREEN}✅ Frontend dependencies already installed${NC}"
fi

# Setup Python virtual environment
if [ ! -d "backend/venv" ]; then
    echo -e "${BLUE}🐍 Setting up Python virtual environment...${NC}"
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd ..
    echo -e "${GREEN}✅ Python environment setup complete${NC}"
else
    echo -e "${GREEN}✅ Python environment already exists${NC}"
fi

echo ""
echo -e "${GREEN}🎉 Setup complete!${NC}"
echo ""
echo -e "${BLUE}Starting servers...${NC}"
echo ""

# Start backend in background
echo -e "${BLUE}🔧 Starting Backend on http://localhost:8000${NC}"
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo -e "${BLUE}🎨 Starting Frontend on http://localhost:3000${NC}"
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo -e "${GREEN}✨ Both servers are starting!${NC}"
echo ""
echo -e "📍 Frontend: ${BLUE}http://localhost:3000${NC}"
echo -e "📍 Backend:  ${BLUE}http://localhost:8000${NC}"
echo -e "📍 API Docs: ${BLUE}http://localhost:8000/docs${NC}"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop all servers${NC}"
echo ""

# Wait for Ctrl+C
trap "echo '' && echo '🛑 Stopping servers...' && kill $BACKEND_PID $FRONTEND_PID && echo '✅ Servers stopped' && exit" INT

# Keep script running
wait

