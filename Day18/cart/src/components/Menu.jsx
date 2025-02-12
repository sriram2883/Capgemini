import React, { useState } from "react";
import { AppBar, Toolbar, Typography, IconButton, Badge, Card, CardContent, Button, Grid, Container, Accordion, AccordionSummary, AccordionDetails, Drawer, Box } from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import data from "../Assets/data.json";

function Menu() {
  const [cartOpen, setCartOpen] = useState(false);
  const [cart, setCart] = useState({});

  const addToCart = (item) => {
    setCart((prevCart) => {
      const newCart = { ...prevCart };
      if (newCart[item.name]) {
        newCart[item.name].quantity += 1;
      } else {
        newCart[item.name] = { ...item, quantity: 1 };
      }
      return newCart;
    });
  };

  const updateCart = (item, amount) => {
    setCart((prevCart) => {
      const newCart = { ...prevCart };
      if (newCart[item.name]) {
        newCart[item.name].quantity += amount;
        if (newCart[item.name].quantity <= 0) {
          delete newCart[item.name];
        }
      }
      return newCart;
    });
  };

  const cartTotal = Object.values(cart).reduce((sum, item) => sum + item.cost * item.quantity, 0);

  return (
    <Container>
      {/* Navbar */}
      <AppBar position="static" sx={{ mb: 3 }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Shoppers
          </Typography>
          <IconButton color="inherit" onClick={() => setCartOpen(true)}>
            <Badge badgeContent={Object.values(cart).reduce((sum, item) => sum + item.quantity, 0)} color="secondary">
              <ShoppingCartIcon fontSize="large" />
            </Badge>
          </IconButton>
        </Toolbar>
      </AppBar>
      
      <Grid container spacing={2}>
        {/* Menu Section - Takes 70% Width */}
        <Grid item xs={12} md={8}>
          <Typography variant="h4" gutterBottom>
            Shopping Menu
          </Typography>
          {Object.entries(data).map(([category, items]) => (
            <Accordion key={category} sx={{ mb: 2 }}>
              <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography variant="h5" color="primary">
                  {category.charAt(0).toUpperCase() + category.slice(1)}
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Grid container spacing={2}>
                  {items.map((item) => (
                    <Grid item xs={12} sm={6} md={4} key={item.name}>
                      <Card elevation={3}>
                        <CardContent>
                          <Typography variant="h6">{item.name}</Typography>
                          <Typography color="textSecondary">${item.cost}</Typography>
                          <Button 
                            variant="contained" 
                            color="primary" 
                            fullWidth 
                            onClick={() => addToCart(item)}
                            sx={{ mt: 1 }}
                          >
                            Add to Cart
                          </Button>
                        </CardContent>
                      </Card>
                    </Grid>
                  ))}
                </Grid>
              </AccordionDetails>
            </Accordion>
          ))}
        </Grid>
      </Grid>
      
      {/* Cart Drawer */}
      <Drawer anchor="right" open={cartOpen} onClose={() => setCartOpen(false)}>
        <Container sx={{ width: 300, padding: 2 }}>
          <Typography variant="h5" gutterBottom>
            Your Cart
          </Typography>
          {Object.keys(cart).length === 0 ? (
            <Typography color="textSecondary">Cart is empty</Typography>
          ) : (
            <>
              {Object.entries(cart).map(([key, item]) => (
                <Card key={key} sx={{ mb: 2 }}>
                  <CardContent>
                    <Typography variant="h6">{item.name}</Typography>
                    <Typography color="textSecondary">${item.cost} x {item.quantity} = ${item.cost * item.quantity}</Typography>
                    <Button 
                      variant="contained" 
                      color="primary" 
                      onClick={() => updateCart(item, 1)}
                      sx={{ mt: 1, mr: 1 }}
                    >
                      +
                    </Button>
                    <Button 
                      variant="contained" 
                      color="secondary" 
                      onClick={() => updateCart(item, -1)}
                      sx={{ mt: 1 }}
                    >
                      -
                    </Button>
                  </CardContent>
                </Card>
              ))}
              <Box sx={{ mt: 2, p: 2, borderTop: "1px solid #ccc", textAlign: "center" }}>
                <Typography variant="h6">Total: ${cartTotal}</Typography>
              </Box>
            </>
          )}
        </Container>
      </Drawer>
    </Container>
  );
}

export default Menu;
