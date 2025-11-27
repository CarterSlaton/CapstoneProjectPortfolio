import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="RouteMaker - Capstone Project Portfolio",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #319795 0%, #3182CE 100%);
        -webkit-background-clip: text;
        text-align: center;
        padding: 1rem 0;
        color: white;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A0AEC0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f7fafc;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #319795;
    }
    .code-block {
        background-color: #1a202c;
        color: #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        overflow-x: auto;
    }
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .tech-badge {
        background-color: #319795;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    div[data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown('<h1 style="color: #E2E8F0;">Route Maker Navigation</h1>', unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "",
    ["🏠 Overview", "🎯 Features", "🏗️ Architecture", "💻 Code Snippets", 
     "📊 Metrics & Testing", "🚀 Deployment", "📱 Screenshots & Video"],
    label_visibility="collapsed"
)

# Overview Page
if page == "🏠 Overview":
    st.markdown('<h1 class="main-header">RouteMaker</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Route Running Planning Application</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Developer", "Carter Slaton")
    with col2:
        st.metric("Tech Stack", "MERN + TypeScript")
    with col3:
        st.metric("Status", "✅ Deployed")
    
    st.markdown("---")
    
    st.header("📖 Project Overview")
    st.write("""
    RouteMaker is a web application that helps runners automatically generate loop routes from their 
    current location, track runs in real-time using mobile GPS, and save detailed run history with 
    complete GPS traces. The system uses Mapbox for mapping and directions, React + TypeScript for 
    the frontend, and a Node/Express backend with MongoDB Atlas for persistence.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Problem Statement")
        st.info("""
        Runners struggle to quickly plan loop routes and reliably record runs with accurate GPS traces 
        and summary metrics. Manual route drawing is complicated and time-consuming, while existing apps 
        often lack complete GPS data persistence.
        """)
    
    with col2:
        st.subheader("💡 Solution")
        st.success("""
        RouteMaker provides automatic loop route generation, real-time GPS tracking with visual feedback, 
        and complete run data persistence to cloud storage. The mobile-first design makes it accessible 
        to all users.
        """)
    
    st.markdown("---")
    
    st.header("🔗 GitHub Link")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button("🔗 GitHub Repository", "https://github.com/CarterSlaton/RouteMaker", use_container_width=True)
    
    st.markdown("---")
    
    st.header("⏱️ Project Timeline")
    timeline_data = {
        "Phase": ["Planning", "Development", "Testing", "Deployment"],
        "Duration": ["Jun 5 - Jul 28", "Aug 1 - Nov 13", "Nov 14 - Nov 15", "Nov 13 - Nov 16"],
        "Status": ["✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete"]
    }
    df_timeline = pd.DataFrame(timeline_data)
    st.dataframe(df_timeline, use_container_width=True, hide_index=True)

# Features Page
elif page == "🎯 Features":
    st.title("🎯 Key Features")
    
    features = [
        {
            "title": "🗺️ Auto-Generate Routes",
            "description": "Create loop routes from user location with target distance (0.5-50 km/mi)",
            "details": [
                "Smart retry logic (up to 3 attempts)",
                "Walkable path optimization",
                "Target accuracy within 7% of requested distance"
            ]
        },
        {
            "title": "📍 Real-Time GPS Tracking",
            "description": "Live position updates with visual feedback",
            "details": [
                "Pulsing runner marker (50px, red #E53E3E)",
                "Red tracking line (6px width, 0.9 opacity)",
                "Update every 5 seconds",
                "Accuracy filtering (≤100m threshold)"
            ]
        },
        {
            "title": "💾 Complete Run Persistence",
            "description": "All GPS points, statistics, and timestamps saved to cloud database",
            "details": [
                "Full GPS trace (not sampled)",
                "Distance, time, pace metrics",
                "Pause timestamps and durations",
                "MongoDB Atlas cloud storage"
            ]
        },
        {
            "title": "📱 Mobile-First Design",
            "description": "Responsive UI optimized for mobile devices",
            "details": [
                "Touch-optimized controls",
                "Hamburger menu navigation",
                "No horizontal scroll or overflow",
                "Simplified 'Generate Route' experience"
            ]
        },
        {
            "title": "☁️ Cloud Deployment",
            "description": "Production-ready infrastructure",
            "details": [
                "Backend on Render",
                "Frontend ready for Vercel",
                "MongoDB Atlas database",
                "Environment-based configuration"
            ]
        },
        {
            "title": "📊 Elevation Profiles",
            "description": "Detailed elevation data and visualization",
            "details": [
                "Min/Max elevation tracking",
                "Total gain and loss calculations",
                "Interactive elevation chart",
                "Unit conversion (metric/imperial)"
            ]
        }
    ]
    
    for i, feature in enumerate(features):
        with st.expander(f"**{feature['title']}**", expanded=(i==0)):
            st.write(f"**{feature['description']}**")
            st.write("")
            st.write("**Key Details:**")
            for detail in feature['details']:
                st.write(f"• {detail}")
    
    st.markdown("---")
    
    st.header("🛠️ Technology Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Frontend")
        techs = ["React 18", "TypeScript", "Vite", "Chakra UI", "Mapbox GL JS", "React Router"]
        for tech in techs:
            st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Backend")
        techs = ["Node.js 18+", "Express", "TypeScript", "MongoDB", "Mongoose", "JWT Auth"]
        for tech in techs:
            st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)
    
    with col3:
        st.subheader("Deployment")
        techs = ["Render", "MongoDB Atlas", "Vercel", "Git/GitHub"]
        for tech in techs:
            st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)

# Architecture Page
elif page == "🏗️ Architecture":
    st.title("🏗️ System Architecture")
    
    st.header("📐 High-Level Architecture")
    
    st.code("""
    ┌─────────────────────────────────────────────────────────────┐
    │                        CLIENT TIER                          │
    │  ┌────────────────────────────────────────────────────┐    │
    │  │         React SPA (Vite + TypeScript)              │    │
    │  │  • Pages: Home, Generate Route, Run Tracking       │    │
    │  │  • Components: RouteMap, ElevationChart, Navbar    │    │
    │  │  • State: AuthContext, useDistanceUnit             │    │
    │  └───────────────────┬────────────────────────────────┘    │
    └────────────────────────┼───────────────────────────────────┘
                             │
                         HTTPS/REST
                             │
    ┌────────────────────────┼───────────────────────────────────┐
    │                        │    SERVER TIER                     │
    │  ┌─────────────────────▼──────────────────────────────┐    │
    │  │      Node.js + Express API (TypeScript)            │    │
    │  │  • Routes: /api/auth, /api/routes, /api/runs       │    │
    │  │  • Middleware: JWT Authentication, Error Handler   │    │
    │  │  • Services: mapboxService (elevation, directions) │    │
    │  └─────────────────────┬──────────────────────────────┘    │
    └────────────────────────┼───────────────────────────────────┘
                             │
                       Mongoose ODM
                             │
    ┌────────────────────────┼───────────────────────────────────┐
    │                        │     DATA TIER                      │
    │  ┌─────────────────────▼──────────────────────────────┐    │
    │  │          MongoDB Atlas (Cloud Database)            │    │
    │  │  • Collections: users, routes, runs                │    │
    │  │  • Indexes: userId, createdAt                      │    │
    │  └────────────────────────────────────────────────────┘    │
    └─────────────────────────────────────────────────────────────┘
                             
    ┌─────────────────────────────────────────────────────────────┐
    │                   EXTERNAL SERVICES                         │
    │  • Mapbox GL JS: Interactive maps, marker rendering         │
    │  • Mapbox Directions API: Route generation                  │
    │  • Mapbox Tilequery API: Elevation data                     │
    │  • Mapbox Geocoding API: Address/location search            │
    └─────────────────────────────────────────────────────────────┘
    """, language="text")
    
    st.markdown("---")
    
    st.header("🔄 Data Flow Diagrams")
    
    tab1, tab2, tab3 = st.tabs(["Route Generation", "GPS Tracking", "Run Persistence"])
    
    with tab1:
        st.subheader("Route Generation Flow")
        st.code("""
        User Input (distance, unit)
              ↓
        Frontend validates input (0.5-50 km/mi)
              ↓
        POST /api/routes with { coordinates, distance, unit }
              ↓
        Backend validates and saves route
              ↓
        Background: Fetch elevation + directions from Mapbox
              ↓
        Update route with elevationData and directions
              ↓
        Frontend polls/refetches route
              ↓
        Display route on map with elevation profile
        """, language="text")
    
    with tab2:
        st.subheader("GPS Tracking Flow")
        st.code("""
        User clicks "Start Run"
              ↓
        navigator.geolocation.watchPosition() activated
              ↓
        GPS position update (every 5 seconds)
              ↓
        Filter: accuracy ≤ 100m
              ↓
        Filter: distance jump ≤ 0.1 km
              ↓
        Add to gpsPoints array
              ↓
        Update map: red line + pulsing marker
              ↓
        Calculate: distance, time, pace
              ↓
        Display live statistics
              ↓
        User clicks "Stop Run"
              ↓
        POST /api/runs/:id/complete with ALL gpsPoints
              ↓
        Save to MongoDB with full GPS trace
        """, language="text")
    
    with tab3:
        st.subheader("Run Data Persistence")
        st.code("""
        Frontend: Complete run with gpsPoints array
              ↓
        POST /api/runs/:id/complete
         {
           gpsPoints: [{lat, lng, timestamp}],
           statistics: {distance, time, pace},
           pauseTimes: [{start, end}]
         }
              ↓
        Backend: Validate and transform data
              ↓
        MongoDB: Save to 'runs' collection
         {
           _id, userId, routeId, 
           gpsPoints: [...],  // ALL points
           statistics: {...},
           pauseTimes: [...],
           createdAt
         }
              ↓
        Return saved run object
              ↓
        Frontend: Navigate to run details page
              ↓
        Display: Map with GPS trace + statistics
        """, language="text")
    
    st.markdown("---")
    
    st.header("🗂️ Database Schema")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("User Model")
        st.code("""
{
  _id: ObjectId,
  name: String,
  email: String (unique),
  password: String (hashed),
  preferredUnit: "km" | "mi",
  createdAt: Date
}
        """, language="javascript")
    
    with col2:
        st.subheader("Route Model")
        st.code("""
{
  _id: ObjectId,
  userId: ObjectId,
  name: String,
  distance: Number,
  coordinates: [[lng, lat]],
  elevationData: {
    elevationGain: Number,
    elevationLoss: Number,
    minElevation: Number,
    maxElevation: Number,
    profile: [{
      distance: Number,
      elevation: Number
    }]
  },
  directions: [String],
  createdAt: Date
}
        """, language="javascript")
    
    with col3:
        st.subheader("Run Model")
        st.code("""
{
  _id: ObjectId,
  userId: ObjectId,
  routeId: ObjectId,
  gpsPoints: [{
    lat: Number,
    lng: Number,
    timestamp: Number
  }],
  statistics: {
    distance: Number,
    time: Number,
    pace: Number
  },
  pauseTimes: [{
    start: Number,
    end: Number
  }],
  createdAt: Date
}
        """, language="javascript")

# Code Snippets Page
elif page == "💻 Code Snippets":
    st.title("💻 Code Snippets")
    
    st.header("🔍 Featured Code Examples")
    
    snippet_category = st.selectbox(
        "Select Category",
        ["GPS Tracking", "Route Generation", "Elevation Processing", 
         "Unit Conversion", "Authentication", "API Routes"]
    )
    
    if snippet_category == "GPS Tracking":
        st.subheader("GPS Tracking with Accuracy Filtering")
        st.write("**File:** `src/utils/gpsTracking.ts`")
        st.code("""
export const startGPSTracking = (
  onPositionUpdate: (position: GPSPosition) => void,
  onError: (error: string) => void
): number => {
  const watchId = navigator.geolocation.watchPosition(
    (position) => {
      const { latitude, longitude, accuracy } = position.coords;
      
      // Filter out inaccurate positions (>100m accuracy)
      if (accuracy > 100) {
        console.warn('GPS accuracy too low:', accuracy);
        return;
      }
      
      const gpsPosition: GPSPosition = {
        lat: latitude,
        lng: longitude,
        accuracy: accuracy,
        timestamp: Date.now()
      };
      
      onPositionUpdate(gpsPosition);
    },
    (error) => {
      console.error('GPS Error:', error);
      onError(`GPS Error: ${error.message}`);
    },
    {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 0
    }
  );
  
  return watchId;
};
        """, language="typescript")
        
        st.subheader("Jump Detection & Distance Calculation")
        st.write("**File:** `src/pages/RunRoute.tsx`")
        st.code("""
// Filter out GPS jumps (segments > 100m between points)
const handlePositionUpdate = (position: GPSPosition) => {
  if (gpsPointsRef.current.length > 0) {
    const lastPoint = gpsPointsRef.current[gpsPointsRef.current.length - 1];
    const jump = calculateDistance(
      lastPoint.lat, lastPoint.lng,
      position.lat, position.lng
    );
    
    // Ignore jumps greater than 100m (0.1 km)
    if (jump > 0.1) {
      console.warn('GPS jump detected:', jump, 'km - ignoring');
      return;
    }
  }
  
  // Add valid point
  setGpsPoints(prev => [...prev, position]);
  gpsPointsRef.current.push(position);
  
  // Calculate cumulative distance
  if (gpsPointsRef.current.length > 1) {
    const newDistance = calculateDistance(
      gpsPointsRef.current[gpsPointsRef.current.length - 2].lat,
      gpsPointsRef.current[gpsPointsRef.current.length - 2].lng,
      position.lat,
      position.lng
    );
    setDistance(prev => prev + newDistance);
  }
};
        """, language="typescript")
    
    elif snippet_category == "Route Generation":
        st.subheader("Auto-Generate Route with Retry Logic")
        st.write("**File:** `src/pages/CreateRoute.tsx`")
        st.code("""
const generateRoute = async () => {
  setIsGenerating(true);
  setError(null);
  
  try {
    const position = await getCurrentPosition();
    const { latitude, longitude } = position.coords;
    
    // Convert distance to meters
    const distanceInKm = preferredUnit === 'mi' 
      ? distance * 1.60934 
      : distance;
    const distanceInMeters = distanceInKm * 1000;
    
    // Generate waypoints for loop route
    const waypoints = generateLoopWaypoints(
      latitude, 
      longitude, 
      distanceInMeters
    );
    
    let attempts = 0;
    let route = null;
    
    // Retry logic (up to 3 attempts)
    while (attempts < 3 && !route) {
      try {
        const response = await api.post('/routes', {
          coordinates: waypoints,
          distance: distanceInKm,
          name: `${distance} ${preferredUnit} Loop`,
        });
        
        route = response.data;
        
        // Check if route is within 7% of target distance
        const actualDistance = route.distance;
        const targetDistance = distanceInKm;
        const difference = Math.abs(actualDistance - targetDistance);
        const percentDiff = (difference / targetDistance) * 100;
        
        if (percentDiff > 7) {
          console.warn(`Route ${percentDiff.toFixed(1)}% off target, retrying...`);
          route = null;
          attempts++;
        }
      } catch (err) {
        attempts++;
        if (attempts >= 3) throw err;
      }
    }
    
    if (route) {
      navigate(`/routes/${route._id}`);
    }
  } catch (err) {
    setError('Failed to generate route. Please try again.');
  } finally {
    setIsGenerating(false);
  }
};
        """, language="typescript")
    
    elif snippet_category == "Elevation Processing":
        st.subheader("Fetch Elevation Data from Mapbox")
        st.write("**File:** `server/src/services/mapboxService.ts`")
        st.code("""
export const getElevationData = async (coordinates: number[][]) => {
  try {
    const elevationProfile: ElevationPoint[] = [];
    let elevationGain = 0;
    let elevationLoss = 0;
    let minElevation = Infinity;
    let maxElevation = -Infinity;
    let cumulativeDistance = 0;
    
    for (let i = 0; i < coordinates.length; i++) {
      const [lng, lat] = coordinates[i];
      
      // Fetch elevation from Mapbox Tilequery API
      const url = `https://api.mapbox.com/v4/mapbox.terrain-rgb/tilequery/${lng},${lat}.json`;
      const response = await axios.get(url, {
        params: {
          layers: 'contour',
          limit: 1,
          access_token: MAPBOX_ACCESS_TOKEN
        }
      });
      
      const elevation = response.data.features[0]?.properties?.ele || 0;
      elevationProfile.push({ distance: cumulativeDistance * 1000, elevation });
      
      // Calculate elevation gain/loss
      if (elevationProfile.length > 1) {
        const prevElevation = elevationProfile[elevationProfile.length - 2].elevation;
        const elevChange = elevation - prevElevation;
        
        if (elevChange > 0) {
          elevationGain += elevChange;
        } else {
          elevationLoss += Math.abs(elevChange);
        }
      }
      
      // Track min/max
      minElevation = Math.min(minElevation, elevation);
      maxElevation = Math.max(maxElevation, elevation);
      
      // Calculate cumulative distance
      if (i > 0) {
        cumulativeDistance += calculateDistance(
          coordinates[i-1][1], coordinates[i-1][0],
          lat, lng
        );
      }
    }
    
    return {
      elevationGain: Math.round(elevationGain),
      elevationLoss: Math.round(elevationLoss),
      minElevation: Math.round(minElevation),
      maxElevation: Math.round(maxElevation),
      profile: elevationProfile
    };
  } catch (error) {
    console.error('Elevation fetch error:', error);
    return null;
  }
};
        """, language="typescript")
    
    elif snippet_category == "Unit Conversion":
        st.subheader("Distance & Elevation Unit Conversion")
        st.write("**File:** `src/utils/unitConversion.ts`")
        st.code("""
export type DistanceUnit = 'km' | 'mi';

// Convert kilometers to miles
export function kmToMiles(km: number): number {
  return km * 0.621371;
}

// Convert miles to kilometers
export function milesToKm(miles: number): number {
  return miles * 1.60934;
}

// Convert meters to feet
export function metersToFeet(meters: number): number {
  return meters * 3.28084;
}

// Format distance with unit
export function formatDistance(
  distanceKm: number, 
  unit: DistanceUnit = 'km'
): string {
  if (unit === 'mi') {
    const miles = kmToMiles(distanceKm);
    return `${miles.toFixed(2)} mi`;
  }
  return `${distanceKm.toFixed(2)} km`;
}

// Format elevation with unit
export function formatElevation(
  elevationMeters: number,
  unit: DistanceUnit = 'km'
): string {
  if (unit === 'mi') {
    const elevationFeet = metersToFeet(elevationMeters);
    return `${Math.round(elevationFeet)} ft`;
  }
  return `${Math.round(elevationMeters)} m`;
}

// Format pace (min/km or min/mi)
export function formatPace(
  paceMinPerKm: number,
  unit: DistanceUnit = 'km'
): string {
  if (unit === 'mi') {
    const paceMinPerMile = paceMinPerKm * 1.60934;
    const minutes = Math.floor(paceMinPerMile);
    const seconds = Math.round((paceMinPerMile - minutes) * 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}/mi`;
  }
  const minutes = Math.floor(paceMinPerKm);
  const seconds = Math.round((paceMinPerKm - minutes) * 60);
  return `${minutes}:${seconds.toString().padStart(2, '0')}/km`;
}
        """, language="typescript")
    
    elif snippet_category == "Authentication":
        st.subheader("JWT Authentication Middleware")
        st.write("**File:** `server/src/middleware/auth.ts`")
        st.code("""
import jwt from 'jsonwebtoken';
import { Request, Response, NextFunction } from 'express';

interface AuthRequest extends Request {
  userId?: string;
}

export const authenticate = (
  req: AuthRequest, 
  res: Response, 
  next: NextFunction
) => {
  try {
    // Get token from header
    const token = req.header('Authorization')?.replace('Bearer ', '');
    
    if (!token) {
      return res.status(401).json({ 
        error: 'No authentication token provided' 
      });
    }
    
    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as { 
      userId: string 
    };
    
    // Attach userId to request
    req.userId = decoded.userId;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid authentication token' });
  }
};
        """, language="typescript")
        
        st.subheader("User Login Route")
        st.write("**File:** `server/src/routes/authRoutes.ts`")
        st.code("""
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import User from '../models/User';

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    // Find user by email
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    // Check password
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    // Generate JWT token
    const token = jwt.sign(
      { userId: user._id }, 
      process.env.JWT_SECRET!,
      { expiresIn: '7d' }
    );
    
    res.json({
      token,
      user: {
        id: user._id,
        name: user.name,
        email: user.email,
        preferredUnit: user.preferredUnit
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Login failed' });
  }
});
        """, language="typescript")
    
    elif snippet_category == "API Routes":
        st.subheader("Route Creation Endpoint")
        st.write("**File:** `server/src/routes/routeRoutes.ts`")
        st.code("""
router.post('/', authenticate, async (req: AuthRequest, res) => {
  try {
    const { coordinates, distance, name } = req.body;
    
    // Validate input
    if (!coordinates || !distance) {
      return res.status(400).json({ 
        error: 'Coordinates and distance required' 
      });
    }
    
    // Create route document
    const route = new Route({
      userId: req.userId,
      name: name || `${distance} km Route`,
      distance,
      coordinates,
      createdAt: new Date()
    });
    
    // Save route first (fast response)
    const savedRoute = await route.save();
    res.status(201).json(savedRoute);
    
    // Fetch elevation data and directions in background
    Promise.all([
      getElevationData(coordinates),
      getDirections(coordinates)
    ]).then(async ([elevationData, directions]) => {
      if (elevationData || directions.length > 0) {
        await Route.findByIdAndUpdate(savedRoute._id, {
          elevationData: elevationData || undefined,
          directions: directions || []
        });
        console.log('Elevation and directions updated:', savedRoute._id);
      }
    }).catch(error => {
      console.error('Error fetching elevation/directions:', error);
    });
    
  } catch (error) {
    res.status(500).json({ error: 'Failed to create route' });
  }
});
        """, language="typescript")

# Metrics & Testing Page
elif page == "📊 Metrics & Testing":
    st.title("📊 Metrics & Testing")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Test Cases", "21")
    with col2:
        st.metric("Requirements", "13")
    with col3:
        st.metric("Pass Rate", "95%")
    with col4:
        st.metric("Code Coverage", "85%")
    
    st.markdown("---")
    
    st.header("🧪 Test Coverage Summary")
    
    test_data = {
        "Test Area": [
            "GPS Tracking",
            "Run Data Persistence",
            "Mobile Responsiveness",
            "Unit Switching",
            "Backend Deployment",
            "Route Generation",
            "Elevation Data"
        ],
        "Status": [
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete"
        ],
        "Test Cases": [
            "TC20-TC21",
            "TC22",
            "TC10",
            "TC15",
            "TC22, TC23",
            "TC02-TC03, TC16",
            "TC17"
        ],
        "Pass Rate": [
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%"
        ]
    }
    
    df_tests = pd.DataFrame(test_data)
    st.dataframe(df_tests, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.header("📈 Performance Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("GPS Tracking Performance")
        perf_data = {
            "Metric": [
                "Update Interval",
                "Average Accuracy",
                "Points per Hour",
                "Jump Filtering"
            ],
            "Value": [
                "5 seconds",
                "50-100 meters",
                "~720 points",
                "Rejects >100m"
            ]
        }
        st.table(pd.DataFrame(perf_data))
    
    with col2:
        st.subheader("System Performance")
        sys_data = {
            "Metric": [
                "Route Generation",
                "API Response Time",
                "Database Query",
                "Frontend Bundle"
            ],
            "Value": [
                "1-5 seconds",
                "200-500ms (p95)",
                "<100ms",
                "1.2 MB (gzipped)"
            ]
        }
        st.table(pd.DataFrame(sys_data))
    
    st.markdown("---")
    
    st.header("🎯 Requirements Traceability")
    
    req_data = {
        "Requirement": [
            "FR1 - Route Generation",
            "FR2 - Run Saving",
            "FR3 - GPS Visualization",
            "FR4 - Data Persistence",
            "FR5 - Run History",
            "FR6 - User Preferences",
            "FR7 - Mobile Support"
        ],
        "Test Cases": [
            "TC02-TC03, TC16",
            "TC22",
            "TC20-TC21",
            "TC19, TC22-TC23",
            "TC22",
            "TC12-TC15",
            "TC10"
        ],
        "Status": [
            "✅ Implemented",
            "✅ Implemented",
            "✅ Implemented",
            "✅ Implemented",
            "✅ Implemented",
            "✅ Implemented",
            "✅ Implemented"
        ],
        "Coverage": [
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%"
        ]
    }
    
    df_reqs = pd.DataFrame(req_data)
    st.dataframe(df_reqs, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.header("📊 Code Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Files", "70+")
        st.metric("Frontend Components", "7")
        st.metric("Pages", "11")
    
    with col2:
        st.metric("API Endpoints", "25+")
        st.metric("Lines of Code", "~12,000")
        st.metric("Models", "3")
    
    with col3:
        st.metric("Test Cases", "21")
        st.metric("Requirements", "13")
        st.metric("Bug Fixes", "8+")

# Deployment Page
elif page == "🚀 Deployment":
    st.title("🚀 Deployment")
    
    st.header("☁️ Deployment Status")
    
    deploy_data = {
        "Component": ["Database", "Frontend", "Repository"],
        "Service": ["MongoDB Atlas", "Vercel", "GitHub"],
        "URL": [
            "routemaker.g5daa9x.mongodb.net",
            "vercel.com/carterslatons-projects/route-maker",
            "github.com/CarterSlaton/RouteMaker"
        ],
        "Status": ["✅ Live", "✅ Live", "✅ Updated"]
    }
    
    df_deploy = pd.DataFrame(deploy_data)
    st.dataframe(df_deploy, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.header("⚙️ Environment Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Backend Environment Variables")
        st.code("""
# Server Configuration
PORT=5000
NODE_ENV=production

# Database
MONGODB_URI=mongodb+srv://...

# Authentication
JWT_SECRET=<secret_key>

# Mapbox API
MAPBOX_ACCESS_TOKEN=<token>

# CORS
FRONTEND_URL=https://routemaker.vercel.app
        """, language="bash")
    
    with col2:
        st.subheader("Frontend Environment Variables")
        st.code("""
# API Configuration
VITE_API_URL=<your-api-url>

# Mapbox Configuration
VITE_MAPBOX_ACCESS_TOKEN=<token>

# Build Configuration
NODE_ENV=production
        """, language="bash")
    
    st.markdown("---")
    
    st.header("🔧 Build Commands")
    
    tab1, tab2 = st.tabs(["Backend", "Frontend"])
    
    with tab1:
        st.subheader("Backend Build & Deploy (Render)")
        st.code("""
# Install dependencies
npm install

# Build TypeScript
npm run build

# Start production server
npm start

# Build command: npm run build
# Start command: npm start
# Root directory: server/
        """, language="bash")
    
    with tab2:
        st.subheader("Frontend Build & Deploy (Vercel)")
        st.code("""
# Install dependencies
npm install

# Build production bundle
npm run build

# Preview locally
npm run preview

# Build command: npm run build
# Output directory: dist
# Root directory: .
        """, language="bash")
    
    st.markdown("---")
    
    st.header("📋 Deployment Checklist")
    
    checklist_items = [
        ("✅", "Backend deployed to Render", True),
        ("✅", "MongoDB Atlas cluster configured", True),
        ("✅", "Environment variables set on Render", True),
        ("✅", "API endpoints tested and working", True),
        ("✅", "CORS configured for frontend domain", True),
        ("🟡", "Frontend deployed to Vercel", False),
        ("🟡", "Custom domain configured (optional)", False),
        ("🟡", "SSL certificates verified", False),
        ("⬜", "Performance monitoring enabled", False),
        ("⬜", "Error tracking configured (Sentry)", False)
    ]
    
    for icon, item, done in checklist_items:
        if done:
            st.success(f"{icon} {item}")
        elif icon == "🟡":
            st.warning(f"{icon} {item}")
        else:
            st.info(f"{icon} {item}")

# Screenshots Page
elif page == "📱 Screenshots & Video":
    st.title("📱 Screenshots & Demos")
    
    st.header("🖼️ Application Screenshots")
    
    screenshot_sections = [
        {
            "title": "🏠 Home Page",
            "description": "Landing page with overview of RouteMaker features",
            "filename": "HomePage.jpg"
        },
        {
            "title": "🗺️ Generate Route Page",
            "description": "Auto-generation interface with large gradient button",
            "filename": "GenerateRoute.jpg"
        },
        {
            "title": "📍 Active Run Tracking",
            "description": "Real-time GPS tracking with pulsing marker",
            "filename": "ActiveRun.png"
        },
        {
            "title": "📊 Run Details",
            "description": "Completed run with GPS trace and statistics",
            "filename": "RunDetails.jpg"
        },
        {
            "title": "📈 Elevation Profile",
            "description": "Interactive elevation chart with min/max/gain/loss",
            "filename": "ElevationProfile.png"
        },
        {
            "title": "📱 Mobile View",
            "description": "Responsive design on mobile device",
            "filename": "MobileView.png"
        },
        {
            "title": "🗂️ Run History",
            "description": "List of all completed runs with filters",
            "filename": "RunHistory.png"
        },
        {
            "title": "⚙️ Settings Page",
            "description": "User preferences and unit selection",
            "filename": "Settings.png"
        }
    ]
    
    import os
    from pathlib import Path
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    assets_dir = script_dir / "assets"
    
    for section in screenshot_sections:
        with st.expander(f"**{section['title']}**", expanded=False):
            st.write(section['description'])
            
            # Construct full path to image
            image_path = assets_dir / section['filename']
            
            if image_path.exists():
                try:
                    from PIL import Image
                    img = Image.open(image_path)
                    st.image(img, caption=section['title'], use_column_width=True)
                except Exception as e:
                    st.error(f"Error loading image: {e}")
                    st.write(f"*Image file: `{section['filename']}`*")
            else:
                st.warning(f"📷 Image not found: `{section['filename']}`")
    
    st.markdown("---")
    
    st.header("🎥 Demonstration Video")
    st.write("A complete video demonstration showcasing all features of RouteMaker.")
    st.video("https://youtu.be/1R995fRQk0I")
    
    st.markdown("---")
    
    st.header("🔗 Project Link")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button("📂 GitHub Repository", "https://github.com/CarterSlaton/RouteMaker", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #718096; padding: 2rem 0;'>
        <p><strong>RouteMaker - Technology Capstone Project</strong></p>
        <p>Developed by Carter Slaton | Grand Canyon University</p>
        <p>November 2025</p>
    </div>
""", unsafe_allow_html=True)
