import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import { displaySummary } from '../backend_services/Service';
import { ListItem, List } from '@material-ui/core';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import PersonPin from '@material-ui/icons/PersonPin';
import Money from '@material-ui/icons/Money';


const styles = theme => ({
  paper: {
    maxWidth: 936,
    margin: 'auto',
    overflow: 'hidden',
  },
  searchBar: {
    borderBottom: '1px solid rgba(0, 0, 0, 0.12)',
  },
  searchInput: {
    fontSize: theme.typography.fontSize,
  },
  block: {
    display: 'block',
  },
  addUser: {
    marginRight: theme.spacing.unit,
  },
  contentWrapper: {
    margin: '40px 16px',
  },
  root: {
    flexGrow: 1,
    maxWidth: 752,
  },
  demo: {
    backgroundColor: theme.palette.background.paper,
  },
  title: {
    margin: `${theme.spacing.unit * 4}px 0 ${theme.spacing.unit * 2}px`,
  }
});

class Content extends Component {
  constructor(props){
    super(props)
    this.state = {
      userId: props.userInfo.getUserId(),
      balance: props.userInfo.getBalance(),
      stocks: props.userInfo.getStocksMap(),
      transactions: null,
      buyTriggers: null,
      sellTriggers: null      
    };

    this.classes = props.classes
    this.displaySummaryCallback = this.displaySummaryCallback.bind(this)  
    this.generateAccountList = this.generateAccountList.bind(this)
    this.generateTransactionList = this.generateTransactionList.bind(this)
    this.generateTriggerList = this.generateTriggerList.bind(this)
  }

  componentDidMount(){
    displaySummary(this.state.userId,(err, response) => {this.displaySummaryCallback(err,response)})
  }

  displaySummaryCallback(err, response){
      if(err){
        console.log(err.message)
      }else {
        var userInfo = response.getUserInfo()
        this.setState(
          {
            balance: userInfo.getBalance(), // TODO(isaac): Remove this once cailan implements displaysummary
            stocks: userInfo.getStocksMap(),
            transactions: response.getTransactionsList(),
            buyTriggers: response.getBuyTriggersList(),
            sellTriggers: response.getSellTriggersList()
          }
        )
      }
  }

  generateAccountList(){
    var stockList = this.state.stocks.keys().arr_
    var itemList = []
    for(var i in stockList) {
      itemList.push(
      <ListItem>
      <ListItemAvatar>
        <Avatar>
          <Money />
        </Avatar>
      </ListItemAvatar>
      <ListItemText primary={stockList[i] + ":  " +  this.state.stocks.get(stockList[i]).toString()}/>
      </ListItem>
      )
    }
    return itemList
  }

  generateTransactionList(){
    var transactionList = []
    for(var i in this.state.transactions){
      var name = this.state.transactions[i].getCommandName()
      var symbol = this.state.transactions[i].getStockSymbol()
      var amount = this.state.transactions[i].getStockAmount()
      var balanceChange = this.state.transactions[i].getBalanceChange()
      var timestamp = this.state.transactions[i].getTimestamp()

      transactionList.push(
        <ListItem>
        <ListItemAvatar>
          <Avatar>
            <PersonPin />
          </Avatar>
        </ListItemAvatar>
        <ListItemText primary={"Command: " + name + " Symbol: " + symbol + " Stock Amount: " + amount + " Balance Change: " + balanceChange.toFixed(2) + " Timestamp: " + timestamp}/>
      </ListItem>
      )
    }
    return transactionList
  }

  generateTriggerList(triggerType){
  var triggerList = []
  var triggers = (triggerType === "buy") ? this.state.buyTriggers : this.state.sellTriggers
  for(var i in triggers){
    var symbol = triggers[i].getSymbol()
    var amount = triggers[i].getAmount()
    var price = triggers[i].getPrice()
    triggerList.push(
    <ListItem>
      <ListItemAvatar>
        <Avatar>
          <PersonPin />
        </Avatar>
      </ListItemAvatar>
      <ListItemText primary={"Symbol: " + symbol + " Amount: " + amount.toFixed(2) + " Price: " + price.toFixed(2) }/>
    </ListItem>
    )
  }
    
  return triggerList
  }

  render(){
    return (
        <Paper className={this.classes.paper}>
      <div className={this.classes.root}>
        <Grid container spacing={16}>
          <Grid item xs={12} md={6}>
            <Typography variant="h6" className={this.classes.title}>
              Account Info
            </Typography>
            <div className={this.classes.demo}>
              <List dense={true}>
                  <ListItem>
                  <ListItemAvatar>
                    <Avatar>
                      <PersonPin />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText primary={"User Id: " + this.state.userId}/>
                </ListItem>
                <ListItem>
                          <ListItemAvatar>
                    <Avatar>
                      <PersonPin />
                    </Avatar>
                  </ListItemAvatar>
                <ListItemText primary={"Balance: " + this.state.balance.toFixed(2)}/>
                </ListItem>
                 {this.generateAccountList()}
              </List>
            </div>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h6" className={this.classes.title}>
              Transactions
            </Typography>
            <div className={this.classes.demo}>
              <List dense={true}>
                {this.generateTransactionList()}
              </List>
            </div>
          </Grid>
        </Grid>
        <Grid container spacing={16}>
          <Grid item xs={12} md={6}>
            <Typography variant="h6" className={this.classes.title}>
              Buy Triggers
            </Typography>
            <div className={this.classes.demo}>
              <List dense={true}>
                {this.generateTriggerList("buy")}
              </List>
            </div>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h6" className={this.classes.title}>
              Sell Triggers
            </Typography>
            <div className={this.classes.demo}>
              <List dense={true}>
                {this.generateTriggerList("sell")}
              </List>
            </div>
          </Grid>
        </Grid>
      </div>
    </Paper>
      );
  }

}

Content.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Content);